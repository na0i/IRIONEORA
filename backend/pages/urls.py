from django.urls import path
from . import views

urlpatterns = [
    path('',views.artifact_recommend)
    # path('', views.review_index_or_create),
    # path('<int:review_pk>/', views.review_detail_or_update_or_delete),
]