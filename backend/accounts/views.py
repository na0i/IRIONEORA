from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

# 중복확인
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
User = get_user_model()


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


# 카카오 로그인
@api_view(['GET'])
def kakao_login(request):
    pass