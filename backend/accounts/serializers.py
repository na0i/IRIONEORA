from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(max_length=10)
    nickname = serializers.CharField(max_length=20)
    email = serializers.EmailField(required=False)
    profile_img = serializers.CharField(required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['profile_img'] = self.validated_data.get('profile_img', '')
        return data_dict


class CustomUserDetailSerializer(UserDetailsSerializer):
    username = serializers.CharField(max_length=10)
    nickname = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', )


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(min_length=1)

    class Meta:
        model = User
        fields = ('username', 'password', )