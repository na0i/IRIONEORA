from rest_framework import serializers
from .models import Artifact


class ArtifactSerializer(serializers.ModelSerializer):
    identification_number = serializers.CharField(max_length=100)
    image_uri = serializers.CharField(min_length=1)

    class Meta:
        model = Artifact
        fields = '__all__'


class ArtifactLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ('like_users')