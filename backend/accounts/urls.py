from django.urls import path, include
from . import views


urlpatterns = [
    path('username/', views.username_duplicate_check),
    path('kakao/login/', views.kakao_login),
    path('kakao/user/', views.KakaoAccountsLogin.as_view()),
    path('', include('allauth.urls')),
]
