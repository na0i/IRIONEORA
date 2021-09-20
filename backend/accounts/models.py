from django.db import models
from django.contrib.auth.models import AbstractUser
from artifacts.models import Artifact


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    profile_img = models.TextField(null=True)
    like_artifact = models.ManyToManyField(Artifact, related_name='like_users')
    resemble_artifact = models.ManyToManyField(Artifact, related_name='resemble_users')

