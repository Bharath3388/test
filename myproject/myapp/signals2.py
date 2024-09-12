#By default, Django signals are executed within the same database transaction as the caller. For example, in the case of post_save, the signal is triggered after the save operation is committed.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal is running within the transaction.")
    else:
        print("Signal is running outside the transaction.")
