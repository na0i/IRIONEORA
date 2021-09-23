from django.urls import path, include
from . import views


urlpatterns = [
    path('username/', views.username_duplicate_check),
    path('kakao/login/', views.kakao_login),
    path('', include('allauth.urls')),
]
