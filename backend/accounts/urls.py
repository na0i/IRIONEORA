from django.urls import path
from . import views


urlpatterns = [
    path('username/', views.username_duplicate_check),
    path('email/', views.email_duplicate_check)
]
