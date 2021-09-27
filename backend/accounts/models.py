from django.db import models
from django.contrib.auth.models import AbstractUser
from artifacts.models import Artifact


# Create your models here.
class User(AbstractUser):
    # 아이디
    username = models.CharField(max_length=10, unique=True)
    # 닉네임
    nickname = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    profile_img = models.TextField(null=True)
    like_artifact = models.ManyToManyField(Artifact, related_name='like_users')
    resemble_artifact = models.ManyToManyField(Artifact, related_name='resemble_users')

