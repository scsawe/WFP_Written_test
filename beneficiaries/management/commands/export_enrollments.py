import csv
from django.core.management.base import BaseCommand
from beneficiaries.models import AssistanceProject, Enrollment, Household, Person


class Command(BaseCommand):
    help = 'Export enrollment summary to CSV'

    def add_arguments(self, parser):
        parser.add_argument('enrollments', help='Output filename')

    def handle(self, *args, **options):
        filename = options['enrollments']
        
        # Retrieve enrollments in the assistance project
        assistance_project = AssistanceProject.objects.get(name="Project 2")
        enrollments = Enrollment.objects.filter(assistance_project=assistance_project)

        # Define CSV headers
        headers = ['Enrollment ID', 'Household ID', 'Household Name', 'Recipient\'s Full Name', 'Cash Offer', 'Phone Number']

        # Create a CSV file and write the data
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

            # Write enrollment data to the CSV file
            for enrollment in enrollments:
                row = [
                    enrollment.id,
                    enrollment.assistance_project,
                    enrollment.household,
                    enrollment.Household.name,
                    enrollment.Person.first_name.get_full_name(),
                    enrollment.cash_offer,
                    enrollment.Person.phone_number
                ]
                writer.writerow(row)

        self.stdout.write(self.style.SUCCESS(f'Enrollment summary exported to {filename}'))
