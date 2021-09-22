# from django.http import response
# from django.shortcuts import get_object_or_404
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
from django.contrib.auth import get_user_model
User = get_user_model()

# constant value
service_key = 'DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg=='

#main_page 1차 완성
@api_view(['GET'])
def artifact_recommend(request):
    #수정: 숫자범위를 sql 데이터 마지막으로 바꿔야함
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

# search page 미완성
#수정: 건의 db에 리스트 저장 vs list to dict 변환작업
#수정: 결과 내 재검색 vs 다중검색 어떻게 할까요????!?
#수정: 예지님과 만든곳에서 어떻게 했지?
@api_view(['GET'])
def artifact_search(request, index_word ):
    # 전체 검색수 파악 및 변수 설정
    url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&name={index_word}&numOfRows=1&pageNo=1'
    response = requests.get(url).content
    response_dict = xmltodict.parse(response)
    # ans_json = json.dumps(ans_dict)
    total_count = int(response_dict["result"]["totalCount"]) // 100
    last_count = int(response_dict["result"]["totalCount"]) % 100

    # 이름에 해당 키워드가 들어간 유물 찾기
    search_list = []
    for i in range(1,total_count+2):
        url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&name={index_word}&numOfRows=100&pageNo={i}'
        print(url)
        response = requests.get(url).content
        response_dict = xmltodict.parse(response)
        print(response_dict["result"]["list"]["data"][1]["item"][6])
        if i == total_count+1:
            print("pass")
            for j in range(0,last_count):
        
                if response_dict["result"]["resultMsg"] == "정보 조회에 실패하였습니다.":
                    print("skip")
                else:
                    search_list.append(response_dict["result"]["list"]["data"][j]["item"][-1]["@value"])
                    # search_list.append(response_dict["result"]["list"]["data"][j]["item"][-17]["@value"])
                    # print("add")
        else:
            # 왜 이런 응답이 나올까?
            for j in range(0,100):
                if response_dict["result"]["resultMsg"] == "정보 조회에 실패하였습니다.":
                    print("skip")
                else:
                    search_list.append(response_dict["result"]["list"]["data"][j]["item"][-1]["@value"])
                    # search_list.append(response_dict["result"]["list"]["data"][j]["item"][-17]["@value"])
                    # print("add")
                    
    # from collections import OrderedDict
    # dict(OrderedDict(val))

    return Response(search_list)

@api_view(['GET'])
def artifact_detail(request,id_num):
    
    # 유물 상세 정보 가져오기
    artifact_url = f"http://www.emuseum.go.kr/openapi/relic/detail?serviceKey={service_key}&id={id_num}"
    url_open = urlopen(artifact_url)
    response_xml = url_open.read().decode('utf-8')
    response_dict = xmltodict.parse(response_xml)
    response_json = json.dumps(response_dict)

    #수정 vue에 필요한 응답을 만들기
    return Response(response_json)
    # return Response(response_dict)


#profile_page
#수정1 유저정보가 어디 저장되는가? 토큰? 세션?
#수정1-1 내가 변수로 같이 보낼까?
#수정1-2 아니면 내가 필터로 찾을까?
#수정1-3 좋아요 테이블이 어떻게 구성되지?
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