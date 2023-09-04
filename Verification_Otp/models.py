from django.db import models
from django.contrib.auth.models import AbstractUser
from Verification_Otp.manager import UserManager2
# Create your models here.

# class CustomUser(AbstractUser):
#     username=None
#     phone_number=models.CharField(max_length=100,unique=True)
#     user_bio=models.CharField(max_length=100)
#     user_profile_image=models.ImageField(upload_to='profile')
    
#     USERNAME_FIELD='phone_number'
#     REQUIRED_FIELDS=[]
#     objects=UserManager()
    
    
    
class User(AbstractUser):
    phone_number=models.CharField(max_length=12,unique=True)
    is_phone_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6)
    
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects=UserManager2()
