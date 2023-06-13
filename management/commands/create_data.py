from django.core.management.base import BaseCommand
from beneficiaries.models import AssistanceProject, Household, Person

class Command(BaseCommand):
    help = 'Create projects and households with members'

    def handle(self, *args, **options):
        # Create projects
        for i in range(5):
            assistanceproject = AssistanceProject.objects.create(name=f'AssistanceProject {i+1}')

            # Create households
            for j in range(10):
                household = Household.objects.create(project=project, name=f'Household {j+1}')

                # Create members
                for k in range(5):
                    Person.objects.create(household=household, name=f'Person {k+1}')

        self.stdout.write(self.style.SUCCESS('Data created successfully.'))
