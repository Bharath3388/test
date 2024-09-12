from django.contrib.auth.models import User
from django.http import HttpResponse
import uuid

def trigger_signal_view(request):
    # Create a unique username using uuid
    unique_username = f"user_{uuid.uuid4()}"
    
    # Create a new user with a unique username
    User.objects.create(username=unique_username)
    
    return HttpResponse(f"Signal Triggered")
