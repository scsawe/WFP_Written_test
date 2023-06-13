from django.core.management.base import BaseCommand
from beneficiaries.models import AssistanceProject, Household

class Command(BaseCommand):
    help = 'Enroll households for an assistance project and offer cash assistance'

    def handle(self, *args, **options):
        project_name = 'Beyond Zero Campaign'  # Specify the name of your assistance project
        amount = 100  # Specify the cash assistance amount

        try:
            project = AssistanceProject.objects.get(name=project_name)
        except AssistanceProject.DoesNotExist:
            self.stderr.write(f"The assistance project '{project_name}' does not exist.")
            return

        households = Household.objects.filter(project=project)[:3]  # Get the first 3 households for enrollment

        for household in households:
            household.cash_assistance = amount
            household.save()

            self.stdout.write(f"Enrolled Household ID: {household.id}, Cash Assistance: ${amount}")

        self.stdout.write(self.style.SUCCESS('Households enrolled successfully.'))
