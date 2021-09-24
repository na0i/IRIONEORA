from rest_framework import serializers
from .models import Artifact

class MainArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = '__all__'
        # exclude = ('user',)