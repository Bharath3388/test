
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals 
        import myapp.signals1
        import myapp.signals2
        import myapp.rectangle
