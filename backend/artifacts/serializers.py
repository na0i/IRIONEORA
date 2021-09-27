from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Artifact, ArtifactDetail


class ArtifactSerializer(serializers.ModelSerializer):
    identification_number = serializers.CharField(max_length=100)
    image_uri = serializers.CharField(min_length=1)

    class Meta:
        model = Artifact
        fields = '__all__'


class ArtifactLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ('like_users', )


class ArtifactResembleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ('resemble_users', )

class ArtifactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactDetail
        fields = '__all__'