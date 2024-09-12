import threading
from django.contrib.auth.models import User
from django.http import HttpResponse
import uuid

def trigger_signal_view(request):
    unique_username = f"user_{uuid.uuid4()}"
    
    User.objects.create(username=unique_username)
    return HttpResponse("Signal Triggered")
