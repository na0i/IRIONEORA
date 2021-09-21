from django.shortcuts import get_object_or_404
from .models import Artifact
from .serializers import ArtifactSerializer
from rest_framework import serializers
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
import random
# from django.contrib.auth import get_user_model

# Create your views here.
# User = get_user_model()

@api_view(['GET'])
def artifact_recommend(request):
    # 숫자범위를 sql 데이터 마지막으로 바꿔야함 
    randomNum = random.randrange(1,1000)
    recomended_artifact = Artifact.objects.filter(identification_number=randomNum)
    serializer = ArtifactSerializer(recomended_artifact, many=True)
    return Response(serializer.data)
       
    # elif request.method == "POST":
    #     print(1)
    #     print(request)
    #     print(request.data)
    #     print(2)
    #     serializer = ReviewSerializer(data = request.data)
    #     my_user =User.objects.filter(username=request.data["UserName"])
    #     # print(1)
    #     # print(request.data)
    #     print(my_user[0].email)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(user=my_user[0], nickname= my_user[0].nickname, username=request.data["UserName"], email=my_user[0].email)
    #         print(serializer.data)
    #         return Response(serializer.data, status= status.HTTP_201_CREATED)         

# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_or_update_or_delete(request, review_pk):
#     review = get_object_or_404(Review, pk = review_pk)

#     if request.method == "GET":
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         print(111)
#         serializer = ReviewSerializer(instance = review , data= request.data)
#         print(serializer)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(review = review)
#             return Response(serializer.data)

#     elif request.method == "DELETE":
#         write_user = Review.objects.filter(id=review.pk)
#         my_user =User.objects.filter(username=request.data["UserName"])
#         # print(request.data["UserName"])
#         # print(write_user[0].username)
#         # print(my_user[0])
#         if str(my_user[0]) == str(write_user[0].username):
#             review.delete()
#             data = {
#                 "success" : True,
#                 "message" : "리뷰삭제"
#             }
#             return Response(data, status=status.HTTP_204_NO_CONTENT)
#         else:
#             data = {
#                 "success" : False,
#                 "message" : "리뷰삭제실패"
#             }
#             return Response(data)