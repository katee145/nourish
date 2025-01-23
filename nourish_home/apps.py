from django.apps import AppConfig

"""
Defines the AppConfig for 'nourish_home'.

    - default_auto_field:
        Specifies the default auto-field for models in the application.
    - 'django.db.models.BigAutoField':
        Sets the default auto-field to BigAutoField.
    - name: Sets the name of the application to 'nourish_home'.
"""


class NourishHomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nourish_home'
