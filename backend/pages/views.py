# from django.http import response
# from django.shortcuts import get_object_or_404
import re
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
import pprint
import bs4
from django.contrib.auth import get_user_model
User = get_user_model()

# constant value
service_key = 'SqZskQNLBydKAJrTV5fUn3zRuenH7ELym5KvJWma15ABpxIYBeQK15yeq+cLDfiGBiMv8Pt5VFk1H0Sz4lX3yw==',
# service_key = 'javtmpZuM82GShOc+dJyc3k5bo3kZ3dGF/eM1wUyCvvLXsbGG/sQz5gR0jfk2hH5OmBCVBPxBl5NqLdcHYv/Ew=='

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

# search page 미완성
#수정: 건의 db에 리스트 저장 vs list to dict 변환작업
@api_view(['GET'])
def artifact_search_index_word(request, index_word):
    # 전체 검색수 파악 및 변수 설정
    url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&index_word={index_word}&numOfRows=1&pageNo=1'
    response = requests.get(url).content
    response_dict = xmltodict.parse(response)
    # ans_json = json.dumps(ans_dict)
    total_count = int(response_dict["result"]["totalCount"]) // 100
    last_count = int(response_dict["result"]["totalCount"]) % 100

    # 이름에 해당 키워드가 들어간 유물 찾기
    search_list = []
    image_uri = ""
    id_num = ""
    name = ""
    
    for i in range(1,total_count+2):
    # for i in range(1,2):
        url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&name={index_word}&numOfRows=100&pageNo={i}'
        # print(url)
        response = requests.get(url)
        response_dict = bs4.BeautifulSoup(response.content, 'html.parser')
        # print("c")
        pprint.pprint(response_dict)
        # for item in response_dict.findAll('item'):
        #     print(item)
        
        for data in response_dict.findAll('data'):
            print("a")
            for item in data.findAll('item'):
                if item['key'] == 'imgUri':
                    image_uri = item['value']
                elif item['key'] == 'id':
                    id_num = item['value']
                elif item['key'] == 'nameKr':
                    name = item['value']
                print("b")
            search_list.append([image_uri,id_num,name])

        # print(search_list)
        # response_dict = xmltodict.parse(response)
        # print(response["item"])
        # if i == total_count+1:
        #     print("pass")
        #     # for j in range(0,last_count):
        
        #     #     if response_dict["result"]["resultMsg"] == "정보 조회에 실패하였습니다.":
        #     #         print("skip")
        #     #     else:
        #     #         search_list.append(response_dict["result"]["list"]["data"][j]["item"][-1]["@value"])
        #     #         # search_list.append(response_dict["result"]["list"]["data"][j]["item"][6]["@value"])
        #     #         # print("add")
        # else:
        #     # 왜 이런 응답이 나올까?
        #     for j in range(0,10):
        #         if response_dict["result"]["resultMsg"] == "정보 조회에 실패하였습니다.":
        #             print("skip")
        #         else:
        #             item = response_dict["result"]["list"]["data"][j]
        #             if item['key'] == 'id':
        #                 search_list.append(item['value'])

                    # search_list.append(response_dict["result"]["list"]["data"][j]["item"][-1]["@value"])
                    # search_list.append(response_dict["result"]["list"]["data"][j]["item"][6]["@value"])
                    # print("add")
                    
    # from collections import OrderedDict
    # print(type(response_dict["result"]["list"]["data"][0]))
    # r = response_dict["result"]["list"]["data"][0]
    # s =dict(OrderedDict(r))
    # print(s["item"])
    # print(type(s["item"]))
    return Response(1)

@api_view(['GET'])
def artifact_search_filter(request,nationalityName2,purposeName2 ):
    # 전체 검색수 파악 및 변수 설정
    url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&purposeName2={purposeName2}&nationalityName2={nationalityName2}&numOfRows=1&pageNo=1'
    response = requests.get(url).content
    response_dict = xmltodict.parse(response)
    # ans_json = json.dumps(ans_dict)
    total_count = int(response_dict["result"]["totalCount"]) // 100
    last_count = int(response_dict["result"]["totalCount"]) % 100

    # 이름에 해당 키워드가 들어간 유물 찾기
    search_list = []
    for i in range(1,total_count+2):
        url =f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&purposeName2={purposeName2}&nationalityName2={nationalityName2}&numOfRows=100&pageNo={i}'
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
                    item = response_dict["result"]["list"]["data"][j]["item"]
                    # search_list.append(response_dict["result"]["list"]["data"][j]["item"][6]["@value"])
                    # print("add")
        else:
            # 왜 이런 응답이 나올까?
            for j in range(0,100):
                if response_dict["result"]["resultMsg"] == "정보 조회에 실패하였습니다.":
                    print("skip")
                else:
                    search_list.append(response_dict["result"]["list"]["data"][j]["item"][-1]["@value"])
                    # search_list.append(response_dict["result"]["list"]["data"][j]["item"][6]["@value"])
                    # print("add")
                    
    # from collections import OrderedDict
    # dict(OrderedDict(val))

    return Response(search_list)


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