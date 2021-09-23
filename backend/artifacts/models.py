from django.db import models
from django.conf import settings


# Create your models here.
class Artifact(models.Model):
    identification_number = models.CharField(max_length=100)
    image_uri = models.TextField()
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_artifact')

