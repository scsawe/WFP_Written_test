from django.db import models
#first_name
#last_name
#household → foreign key to household
#phone_number
#is_recipient – boolean defining whether the person is the designated recipient of the household. He/she will receive the case on behave of the household.

# Create your models here.
class Household(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
     
class Person(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=100)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)#household primary key
    is_recipient = models.CharField(max_length=100)
    # Add more fields as per your requirements
    
class AssistanceProject(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    start_date = models.DateField(max_length=100)
    end_date = models.DateField(max_length=100)

class Enrollment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    assistance_project = models.ForeignKey(AssistanceProject, on_delete=models.CASCADE)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    cash_offer = models.DecimalField(max_digits=10, decimal_places=2)
    #date = models.DateField(auto_now_add=True)
    # Add more fields as per your requirements


    

    
    

