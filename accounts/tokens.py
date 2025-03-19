import uuid
from django.core.cache import cache  # You can also use your database instead of cache

def generate_reset_token(user):
    token = str(uuid.uuid4())
    cache.set(token, user.id, timeout=3600)  # Token valid for 1 hour
    return token

def validate_reset_token(token):
    user_id = cache.get(token)
    if user_id:
        from django.contrib.auth.models import User
        return User.objects.get(id=user_id)
    return None
