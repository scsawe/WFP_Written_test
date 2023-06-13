from django.contrib import admin

# Register your models here.
from beneficiaries.models import Household, Person, AssistanceProject, Enrollment

admin.site.register(Household)
admin.site.register(Person)
admin.site.register(AssistanceProject)
admin.site.register(Enrollment)
