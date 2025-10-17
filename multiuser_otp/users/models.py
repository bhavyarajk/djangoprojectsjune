from django.db import models

from django.contrib.auth.models import AbstractUser

import random
class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=20,null=True)
    is_verified=models.BooleanField(default=False) #to check whether user account is verified or not
    otp=models.CharField(max_length=10,null=True) #to store otp in backend table(CustomUser)

    def generate_otp(self):
        #for creating otp for a user object
        otp=str(random.randint(1000,9999))+str(self.id)
        self.otp=otp
        self.save()





