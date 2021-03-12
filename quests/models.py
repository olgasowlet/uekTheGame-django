from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# from rest_framework_simplejwt.state import User

# Create your models here.

from quests.constants import CATEGORIES, TYPES


class Quest(models.Model):
    unique_number = models.CharField(max_length=4, primary_key=True)
    category = models.CharField(max_length=1, choices=CATEGORIES)
    type = models.CharField(max_length=2, choices=TYPES)
    name = models.CharField(max_length=256)
    credits = models.CharField(max_length=5)
    terms = models.CharField(max_length=256)
    # approved = models.BooleanField(default=False)

