from django.core.management.base import BaseCommand
from beneficiaries.models import AssistanceProject, Household, Person, Enrollment

class Command(BaseCommand):
    help = 'Displays the count of registered beneficiaries'

    def handle(self, *args, **options):
        count = Beneficiary.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Total registered beneficiaries: {count}'))
        
default_app_config = 'beneficiaries.apps.BeneficiariesConfig'