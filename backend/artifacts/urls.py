from django.urls import path
from . import views

urlpatterns = [
    path('artifact_recommend/',views.artifact_recommend)
]