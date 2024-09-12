#By default, Django signals are executed synchronously. This means that the signal handler is invoked immediately after the signal is sent, and the sender has to wait for the handler to complete its execution before proceeding.
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received!")
    time.sleep(5)  # Simulating a delay
    print("Signal processed after delay")
