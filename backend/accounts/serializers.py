from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer, LoginSerializer
from django.contrib.auth import get_user_model

from artifacts.serializers import ArtifactSerializer

User = get_user_model()


# 회원가입
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


# drf user 정보
class CustomUserDetailSerializer(UserDetailsSerializer):
    username = serializers.CharField(max_length=10)
    nickname = serializers.CharField(max_length=20)
    profile_img = serializers.CharField()
    like_artifact = ArtifactSerializer(many=True, read_only=True)
    resemble_artifact = ArtifactSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'profile_img', 'like_artifact', 'resemble_artifact', )


# 로그인
class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(max_length=10)
    password = serializers.CharField(min_length=1)

    class Meta:
        model = User
        fields = ('username', 'password', )

