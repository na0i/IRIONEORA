from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
import requests

# 중복확인
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
User = get_user_model()

# 카카오 로그인
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.models import SocialAccount


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


class KakaoAccountsLogin(SocialLoginView):
    adapter_class = kakao_views.KakaoOAuth2Adapter
    client_class = OAuth2Client


# 카카오 로그인
@api_view(['GET', 'POST'])
def kakao_login(request):

    REST_API_KEY = '0e63d9a73b29cb9e1c85f0279f834367'
    REDIRECT_URI = 'http://localhost:8000/accounts/kakao/login/'

    # 인증 코드 요청 성공
    if request.GET.get('code'):
        print('get code success')
        print(request.GET['code'])
        code = request.GET.get('code')

        # 토큰 요청
        get_token = f'https://kauth.kakao.com/oauth/token'
        params = {
            'grant_type': 'authorization_code',
            'client_id': REST_API_KEY,
            'redirect_uri': REDIRECT_URI,
            'code': code,
        }
        token_res = requests.post(get_token, params=params)
        print(token_res.json())
        access_token = token_res.json()['access_token']

        # 프로필 요청
        get_profile = f'https://kapi.kakao.com/v2/user/me'
        header = {
            'Authorization': f'Bearer {access_token}'
        }

        profile_res = requests.get(get_profile, headers=header)
        print(profile_res.json())

        data = {
            'code': code,
            'access_token': access_token
        }
        print(data)
        # 로그인
        print(SocialAccount.objects.all().values())
        if SocialAccount.objects.all().filter(uid=profile_res.json()['id']):
            print('already in')
            accept = requests.post(f'http://localhost:8000/accounts/kakao/user/', data=data)
            print(accept.json())
        # 회원가입
        else:
            print('need signup')
            accept = requests.post(f'http://localhost:8000/accounts/kakao/user/', data=data)
            print(accept)
            print(accept.json())
            return


    # 카카오 로그인 인증 코드 요청
    else:
        kakao_redirect = f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code'
        return redirect(kakao_redirect)




