from django.db import models

# Create your models here.
class MainArtifact(models.Model):
    identification_number = models.CharField(max_length=100)
    image_uri = models.TextField()





