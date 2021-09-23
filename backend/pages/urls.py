from django.urls import path
from . import views

urlpatterns = [
    path('recommend',views.artifact_recommend),
    path('search/<str:index_word>/',views.artifact_search_index_word),
    path('search/<str:nationalityName2>/<str:purposeName2>/',views.artifact_search_filter),
    path('detail/<str:id_num>/',views.artifact_detail),
    # path('', views.review_index_or_create),
    # path('<int:review_pk>/', views.review_detail_or_update_or_delete),
]