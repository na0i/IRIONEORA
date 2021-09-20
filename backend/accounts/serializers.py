from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(max_length=10, unique=True)
    password = serializers.CharField(max_length=20)
    profile_img = serializers.CharField(required=False, null=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['profile_img'] = self.validated_data.get('profile_img', '')
        return data_dict


class CustomUserDetailSerializer(UserDetailsSerializer):
    username = serializers.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('id', 'username', )