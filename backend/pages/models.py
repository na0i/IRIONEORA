from django.db import models
from artifacts.models import Artifact

# Create your models here.
class Artifact(Artifact):
    pass
    # identification_number = models.CharField(max_length=100)
    # image_uri = models.TextField()
    # desc = models.TextField()
    # museum_name = models.CharField(max_length=200, null=True, blank=True)
    # nationality_name = models.CharField(max_length=200, null=True, blank=True)
    # artifact_name = models.CharField(max_length=200, null=True, blank=True)


# class MainArtifact(models.Model):
#     identification_number = models.CharField(max_length=100)
#     image_uri = models.TextField()
#     desc = models.TextField()
#     museum_name = models.CharField(max_length=200, null=True, blank=True)
#     nationality_name = models.CharField(max_length=200, null=True, blank=True)
#     artifact_name = models.CharField(max_length=200, null=True, blank=True)








