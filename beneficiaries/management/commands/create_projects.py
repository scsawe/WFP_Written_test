from django.core.management.base import BaseCommand
from beneficiaries.models import AssistanceProject
from datetime import datetime

class Command(BaseCommand):
    help = 'Create 5 projects for beneficiaries'

    def handle(self, *args, **options):
        project_data = [
            {
                'name': 'Project 1',
                'start_date': datetime(2023, 1, 1),
                'end_date': datetime(2023, 6, 30)
            },
            {
                'name': 'Project 2',
                'start_date': datetime(2023, 2, 1),
                'end_date': datetime(2023, 7, 31)
            },
            {
                'name': 'Project 3',
                'start_date': datetime(2023, 3, 1),
                'end_date': datetime(2023, 8, 31)
            },
            {
                'name': 'Project 4',
                'start_date': datetime(2023, 4, 1),
                'end_date': datetime(2023, 9, 30)
            },
            {
                'name': 'Project 5',
                'start_date': datetime(2023, 5, 1),
                'end_date': datetime(2023, 10, 31)
            },
        ]

        for data in project_data:
            AssistanceProject.objects.create(              
                name=data['name'],
                start_date=data['start_date'],
                end_date=data['end_date']
            )

        self.stdout.write(self.style.SUCCESS('Projects created successfully.'))
