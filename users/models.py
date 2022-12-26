#from django.db import models
#from django.contrib.auth.models import AbstractUser


##class User(AbstractUser):
    # Add any additional fields you need here
  #  pass


#Create forms: for signup and profile update:

    # Create your models here.
# In the models.py file within your app (users/models.py), define the models for your individual and corporate accounts:

from django.db import models


class IndividualAccount(models.Model):
    # Fields for storing the user's information
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    # Other relevant fields as needed

class CorporateAccount(models.Model):
    # Fields for storing the user's information
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    # Other relevant fields as needed
