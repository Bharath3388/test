#Yes, Django signals run in the same thread as the caller unless explicitly made asynchronous by using threading or other concurrency mechanisms.
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")
