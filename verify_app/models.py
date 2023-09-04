from django.db import models
import random
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=12)
    
