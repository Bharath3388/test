from django.contrib.auth.models import User
from django.http import HttpResponse

def trigger_signal_view(request):
    User.objects.create(username="testuser")  # This will trigger post_save signal
    return HttpResponse("Signal Triggered")


import threading

def trigger_signal_view1(request):
    print(f"Caller thread: {threading.current_thread().name}")
    User.objects.create(username="testuser")
    return HttpResponse("Signal Triggered")





from django.db import transaction


def trigger_signal_view2(request):
    with transaction.atomic():
        User.objects.create(username="testuser")
    return HttpResponse("Signal Triggered")
