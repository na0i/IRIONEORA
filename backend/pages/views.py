from django.http import response
from django.shortcuts import get_object_or_404
from artifacts.models import Artifact
# from artifacts.serializers import ArtifactSerializer
# from .serializers import MainArtifactSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework import status
# from django.db import models

# sell use
from urllib.request import urlopen
import random, requests, json
import xmltodict
# from django.contrib.auth import get_user_model

# Create your views here.
# User = get_user_model()

# constant value
service_key = 'DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg=='

#main_page
@api_view(['GET'])
def artifact_recommend(request):
    #수정 숫자범위를 sql 데이터 마지막으로 바꿔야함
    # 랜덤 추천 유물 선정
    random_num = random.randrange(1,100)
    recommended_artifact = Artifact.objects.filter(id=random_num)
    recommended_artifact_num = recommended_artifact[0].identification_number
    
    # url에서 유물 데이터 수신 후 json 데이터 전송
    artifact_url = f"http://www.emuseum.go.kr/openapi/relic/detail?serviceKey={service_key}&id={recommended_artifact_num}"
    url_open = urlopen(artifact_url)
    response_xml = url_open.read().decode('utf-8')
    response_dict = xmltodict.parse(response_xml)
    response_json = json.dumps(response_dict)

    #수정 vue에 필요한 응답을 만들기
    return Response(response_json)

#profile_page
#수정1 유저정보가 어디 저장되는가? 토큰? 세션?
#수정1-1 내가 변수로 같이 보낼까?
#수정1-2 아니면 내가 필터로 찾을까?
# @api_view(['GET'])
# def artifact_like(request, user_pk ):
#     like_artifacts = UserLikeArtifact.objects.filter(user_id = user_pk)
#     serializer = UserLikeArtifactSerializer(like_artifacts)
#     return Response(serializer.data)

# @api_view(['GET'])
# def artifact_resemble(request, user_pk ):
#     resemble_artifacts = UserResembleArtifact.objects.filter(user_id = user_pk)
#     serializer = UserResembleArtifactSerializer(resemble_artifacts)
#     return Response(serializer.data)

# search page
# @api_view(['POST'])
# def artifact_search(request, index_word ):
#     for i in range(0,500):
#         url = 'http://www.emuseum.go.kr/openapi/relic/list?serviceKey=인증키&name=백제&numOfRows=3&pageNo='+str(i)
#     searched_artifacts = UserResembleArtifact.objects.filter()
#     serializer = UserResembleArtifactSerializer(resemble_artifacts)
#     return Response(serializer.data)
 