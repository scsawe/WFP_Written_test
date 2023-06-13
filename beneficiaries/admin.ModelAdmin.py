from django.contrib import admin
from beneficiaries.models import Household, Person, AssistanceProject, Enrollment

class Household(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')  # Customize the fields displayed in the list view
    search_fields = ('id', 'name', 'location')  # Enable search by name and address

class Person(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number','household','is_recipient')  # Customize the fields displayed in the list view
    list_filter = ('household','is_recipient')  # Add a filter by date
    
class AssistanceProject(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date')  # Customize the fields displayed in the list view
    list_filter = ('start_date','end_date','name')  # Add a filter by date

class Enrollment(admin.ModelAdmin):
    list_display = ('id', 'assistance_project', 'household','cash_offer')  # Customize the fields displayed in the list view
    list_filter = ('assistance_project','household')  # Add a filter by date

admin.site.register(Household, HouseholdAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(AssistanceProject, AssistanceProjectAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
