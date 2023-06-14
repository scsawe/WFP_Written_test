from django.core.management.base import BaseCommand
from beneficiaries.models import AssistanceProject, Household, Enrollment


class Command(BaseCommand):
    help = 'Enroll households in an assistance project'

    def handle(self, *args, **options):
        # Step 1: Retrieve the assistance project
        assistance_project = AssistanceProject.objects.get(name="Project 2")

        # Step 2: Create households
        household1 = Household.objects.create(name="Household 1")
        household2 = Household.objects.create(name="Household 2")
        household3 = Household.objects.create(name="Household 3")

        # Step 3: Enroll households in the assistance project
        household1.assistance_project = assistance_project
        household1.cash_offer = '$100'
        household1.save()

        household2.assistance_project = assistance_project
        household2.cash_offer = '$100'
        household2.save()

        household3.assistance_project = assistance_project
        household3.cash_offer = '$100'
        household3.save()

        self.stdout.write(self.style.SUCCESS('Enrollment successful!'))
