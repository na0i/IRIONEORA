from django.urls import path
from . import views

urlpatterns = [
    path('test',views.test),
    path('userface', views.user_face),
]