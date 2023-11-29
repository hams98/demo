import io
import random
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class SignupModel(models.Model):
    form_username = models.CharField(max_length=24, default='username')
    form_password = models.CharField(max_length=24, default='password')
    form_confirm_password = models.CharField(max_length=24, default='confirm_password')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    registration_datetime = models.DateTimeField(default=timezone.now)  # Use timezone.now as the default value
    action_performed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.registration_datetime:
            self.registration_datetime = timezone.now()
        super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
   

class NoValueModel(models.Model):
    signup = models.ForeignKey('mysite.SignupModel', on_delete=models.CASCADE, null=True, default=None)
    digit_field = models.IntegerField(choices=[(i, str(i)) for i in range(4)])
    form_value = models.CharField(max_length=100)
    interests = models.CharField(max_length=200)
    format_importance = models.CharField(max_length=200)
    catchphrase = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.digit_field = random.randint(1, 4)
        super().save(*args, **kwargs)
        self.update_or_create_user_profile()

    def update_or_create_user_profile(self):
        if self.signup and self.signup.user:
            profile, _ = Profile.objects.get_or_create(user=self.signup.user)
            profile.interests = self.interests
            profile.value = self.format_importance  # Corrected field name
            profile.catchphrase = self.catchphrase
            profile.save()


class ValueModel(models.Model):
    signup = models.ForeignKey('mysite.SignupModel', on_delete=models.CASCADE, null=True, default=None)
    digit_field = models.IntegerField(choices=[(i, str(i)) for i in range(4)])
    form_value = models.CharField(max_length=100)
    interests = models.CharField(max_length=200)
    value_importance = models.CharField(max_length=200)
    catchphrase = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
        self.digit_field = random.randint(1, 4)
        super().save(*args, **kwargs)
        
        if self.signup and self.signup.user:
            print("Updating user profile for user:", self.signup.user.username)
            profile, created = Profile.objects.get_or_create(user=self.signup.user)
            print("Profile created:", created)
            profile.interests = self.interests
            profile.value = self.value_importance
            profile.catchphrase = self.catchphrase
            profile.save()
            print("Profile updated successfully")


class WordleEntry(models.Model):
    signup = models.ForeignKey(SignupModel, on_delete=models.CASCADE, null=True, default=None)
    value = models.ForeignKey(ValueModel, on_delete=models.CASCADE, null=True, default=None)
    letter_1 = models.CharField(max_length=1)
    letter_2 = models.CharField(max_length=1)
    letter_3 = models.CharField(max_length=1)
    letter_4 = models.CharField(max_length=1)
    letter_5 = models.CharField(max_length=1)
    image_data = models.TextField()

    def generate_image(self):
        # Logic to generate the image based on self.form_value
        image = Image.new('RGB', (100, 100), (255, 255, 255))
        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format='PNG')
        image_name = f"{self.form_value}.png"
        image_file = InMemoryUploadedFile(
            image_byte_array, None, image_name, 'image/png', image_byte_array.tell(), None
        )
        self.image_data = image_file.read()
        return image_file


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    interests = models.CharField(max_length=20000)
    value = models.CharField(max_length=20000, default='your_default_value_here')
    catchphrase = models.CharField(max_length=20000)


class Post(models.Model):
    text = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_time = models.DateTimeField(auto_now_add=True)
