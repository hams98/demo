from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import SignupModel

class Backend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if a user with the provided username exists
            user = User.objects.get(username=username)
            print("User found with username:", username)
            return user
        except User.DoesNotExist:
            print("User not found with username:", username)
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
