from django.db import models
from django.conf import settings


# Create your models here.
class Artifact(models.Model):
    identification_number = models.CharField(max_length=100)
    image_uri = models.TextField()

class ArtifactDetail(models.Model):
    identification_number = models.CharField(max_length=100)
    artifact_name = models.CharField(max_length=100)
    artifact_size = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    museum_name = models.CharField(max_length=20)
    index_word = models.TextField(blank=True)
    nationality_name = models.CharField(max_length=50)
    image_uri = models.TextField()