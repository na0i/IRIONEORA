from django.urls import path, include
from . import views


urlpatterns = [
    path('username/', views.username_duplicate_check),
    # path('kakao/login/callback/', ),
    path('', include('allauth.urls')),
]
