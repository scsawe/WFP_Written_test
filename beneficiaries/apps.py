from django.apps import AppConfig


class BeneficiariesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'beneficiaries'
    
# Set the default app config
default_app_config = 'beneficiaries.apps.BeneficiariesConfig'