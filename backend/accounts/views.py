from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from django.shortcuts import render

# 이메일 재전송 관련
from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.permissions import (AllowAny)
from allauth.account.models import EmailAddress
from django.utils.translation import ugettext_lazy as _

# 중복확인
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
User = get_user_model()


# 이메일 인증 완료시 프론트 메인으로 이동
def redirect_to_vue(request):
    return render(request, 'signup_complete.html')


# 회원가입시 닉네임 중복 확인
@api_view(['GET'])
def username_duplicate_check(request):
    username = request.GET['username']
    data = {
        'error': True,
        'result': '이미 사용중인 닉네임입니다.'
    }

    if not User.objects.all().filter(username=username):
        data['error'] = False
        data['result'] = '사용 가능한 닉네임입니다.'

    return Response(data=data)


# 회원가입시 이메일 중복 확인
@api_view(['GET'])
def email_duplicate_check(request):
    email = request.GET['email']
    data = {
        'error': True,
        'result': '이미 사용중인 이메일입니다.'
    }
    if not User.objects.all().filter(email=email):
        data['error'] = False
        data['result'] = '사용 가능한 이메일입니다.'
    return Response(data=data)


class ConfirmEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        # A React Router Route will handle the failure scenario
        return HttpResponseRedirect('/login/success/')

    def get_object(self, queryset=None):
        key = self.kwargs['key']
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                # A React Router Route will handle the failure scenario
                return HttpResponseRedirect('/login/failure/')
        return email_confirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs


# 이메일 재전송 기능
class ResendEmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResendEmailVerification(GenericAPIView):
    serializer_class = ResendEmailVerificationSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']

        try:
            email_address = EmailAddress.objects.get(email__exact=email, verified=False)
            email_address.send_confirmation(self.request, True)
        except EmailAddress.DoesNotExist:
            pass

        return Response({'detail': _('Verification e-mail sent.')})