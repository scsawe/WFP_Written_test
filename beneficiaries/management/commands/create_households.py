from django.core.management.base import BaseCommand
#from beneficiaries.models import Household, HouseholdMember
from beneficiaries.models import Household, Person

class Command(BaseCommand):
    help = 'Create 10 households with at least 5 members in each'

    def handle(self, *args, **options):
        households_data = [
            {
                'household_name': 'Household 1',
                'members': [
                    {
                        'first_name': 'mary',
                        'last_name': 'sawe',
                        'phone_number': 12345678,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'daniel',
                        'last_name': 'sawe',
                        'phone_number': 1234567822,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'Eliud',
                        'last_name': 'sawe',
                        'phone_number': 1234567833,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'christopher',
                        'last_name': 'sawe',
                        'phone_number': 1234567855,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            {
                'household_name': 'Household 2',
                'members': [
                    {
                        'first_name': 'john',
                        'last_name': 'sowe',
                        'phone_number': 1234567892,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'dan',
                        'last_name': 'sawe',
                        'phone_number': 123456,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'lydia',
                        'last_name': 'sawe',
                        'phone_number': 1234567,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'masika',
                        'last_name': 'sawe',
                        'phone_number': 1234567892556,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            {
                'household_name': 'Household 3',
                'members': [
                    {
                        'first_name': 'joy',
                        'last_name': 'sawe',
                        'phone_number': 12345678936666,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'christine',
                        'last_name': 'sawe',
                        'phone_number': 1234567893777,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'bobson',
                        'last_name': 'sawe',
                        'phone_number': 1234567893888,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'kilian',
                        'last_name': 'sawe',
                        'phone_number': 1234567893889,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            {
                'household_name': 'Household 4',
                'members': [
                    {
                        'first_name': 'wyclif',
                        'last_name': 'sawe',
                        'phone_number': 123456789534,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'jame',
                        'last_name': 'sawe',
                        'phone_number': 123456789543,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'peter',
                        'last_name': 'sawe',
                        'phone_number': 123456789553,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'dany',
                        'last_name': 'sawe',
                        'phone_number': 123456789535,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            {
                'household_name': 'Household 5',
                'members': [
                    {
                        'first_name': 'moses',
                        'last_name': 'sawe',
                        'phone_number': 123456789687,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'monicah',
                        'last_name': 'sawe',
                        'phone_number': 123456789678,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'bary',
                        'last_name': 'sawe',
                        'phone_number': 123456789693,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'simon',
                        'last_name': 'sawe',
                        'phone_number': 1234567896456,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            {
                'household_name': 'Household 6',
                'members': [
                    {
                        'first_name': 'brian',
                        'last_name': 'sawe',
                        'phone_number': 123456787,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'seth',
                        'last_name': 'sawe',
                        'phone_number': 123456797,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'peace',
                        'last_name': 'sawe',
                        'phone_number': 123457897,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'patience',
                        'last_name': 'sawe',
                        'phone_number': 123467897,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            {
                'household_name': 'Household 7',
                'members': [
                    {
                        'first_name': 'michael',
                        'last_name': 'sawe',
                        'phone_number': 123567898,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'maureen',
                        'last_name': 'sawe',
                        'phone_number': 124567898,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'macdonal',
                        'last_name': 'sawe',
                        'phone_number': 134567898,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'caleb',
                        'last_name': 'sawe',
                        'phone_number': 234567898,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            {
                'household_name': 'Household 8',
                'members': [
                    {
                        'first_name': 'winy',
                        'last_name': 'sawe',
                        'phone_number': 1234567893,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'joan',
                        'last_name': 'sawe',
                        'phone_number': 123467890,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'jacinta',
                        'last_name': 'sawe',
                        'phone_number': 1234567891,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'william',
                        'last_name': 'sawe',
                        'phone_number': 1234567992,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            {
                'household_name': 'Household 9',
                'members': [
                    {
                        'first_name': 'shadrak',
                        'last_name': 'sawe',
                        'phone_number': 1234789201,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'joash',
                        'last_name': 'sawe',
                        'phone_number': 1234589201,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'levi',
                        'last_name': 'sawe',
                        'phone_number': 1234567201,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'joshua',
                        'last_name': 'sawe',
                        'phone_number': 1234567801,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            {
                'household_name': 'Household 10',
                'members': [
                    {
                        'first_name': 'sheila',
                        'last_name': 'sawe',
                        'phone_number': 1236787891,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'blessings',
                        'last_name': 'sawe',
                        'phone_number': 1234567091,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'emanuel',
                        'last_name': 'sawe',
                        'phone_number': 1234567866,
                        'is_recipient': 'no'
                    },
                    {
                        'first_name': 'faith',
                        'last_name': 'sawe',
                        'phone_number': 1234567906,
                        'is_recipient': 'no'
                    }
                    # Add more members here
                ]
            },
            # Add more households here
        ]

        for household_data in households_data:
           # household = Household.objects.create(name=household_data['household_name'])
            household_name = household_data['household_name']
            household, created = Household.objects.get_or_create(name=household_name)
            members_data = household_data['members']
            for member_data in members_data:
                Person.objects.create(
                    first_name=member_data['first_name'],
                    last_name=member_data['last_name'],
                    phone_number=member_data['phone_number'],
                    household=household,
                    is_recipient=member_data['is_recipient']
                )

        self.stdout.write(self.style.SUCCESS('Households and members created successfully.'))
