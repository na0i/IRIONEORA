# from django.http import response
# from django.shortcuts import get_object_or_404
import re
from artifacts.models import Artifact
from artifacts.serializers import ArtifactSerializer
# from .serializers import MainArtifactSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
# from rest_framework import serializers
# from rest_framework import status
# from django.db import models

from django.core import serializers
from django.http import JsonResponse

# sell use
from urllib.request import urlopen
import random, requests, json
import xmltodict
import pprint
import bs4
from django.contrib.auth import get_user_model
User = get_user_model()

# constant value
service_key = "DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg=="

#main_page 1차 완성
@api_view(['GET'])
def artifact_recommend(request):
    #수정: 숫자범위를 sql 데이터 마지막으로 바꿔야함
    # 랜덤 추천 유물 선정
    random_num = random.randrange(1,100)
    recommended_artifact = Artifact.objects.filter(id=random_num)
    # data = {
    #     'identificationNumber': recommended_artifact[0].identification_number,
    #     'imageUri': recommended_artifact[0].image_uri
    # }
    # return JsonResponse(data=data)
    # print(serializer)
    recommended_artifact_num = recommended_artifact[0].identification_number

    # url에서 유물 데이터 수신 후 json 데이터 전송
    artifact_url = f"http://www.emuseum.go.kr/openapi/relic/detail?serviceKey={service_key}&id={recommended_artifact_num}"
    url_open = urlopen(artifact_url)
    response_xml = url_open.read().decode('utf-8')
    response_dict = xmltodict.parse(response_xml)
    print(response_dict)
    response_json = json.dumps(response_dict)
    print(type(response_json))

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

# search page 완성
@api_view(['GET'])
def artifact_search_index_word(request, index_word):
    # 전체 검색수 파악 및 변수 설정
    url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&indexWord={index_word}&numOfRows=1&pageNo=1'
    response = requests.get(url).content
    response_dict = xmltodict.parse(response)
    total_count = int(response_dict["result"]["totalCount"]) // 100

    # 이름에 해당 키워드가 들어간 유물 찾기
    search_list = []
    image_uri = ""
    id_num = ""
    name = ""
    for i in range(1,total_count+2):
        url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&indexWord={index_word}&numOfRows=100&pageNo={i}'
        response = requests.get(url)
        response_dict = bs4.BeautifulSoup(response.content, 'html.parser')

        for data in response_dict.findAll('data'):
            for item in data.findAll('item'):
                if item['key'] == 'id':
                    id_num = item['value']
                elif item['key'] == 'nameKr':
                    name = item['value']
                elif item['key'] == 'imgUri':
                    image_uri = item['value']
            search_list.append([image_uri,id_num,name])

    return Response(search_list)

@api_view(['GET'])
def artifact_search_filter(request,nationalityName2,purposeName2 ):
    # 전체 검색수 파악 및 변수 설정
    url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&purposeName2={purposeName2}&nationalityName2={nationalityName2}&numOfRows=1&pageNo=1'
    response = requests.get(url).content
    response_dict = xmltodict.parse(response)
    total_count = int(response_dict["result"]["totalCount"]) // 100


    # 이름에 해당 키워드가 들어간 유물 찾기
    search_list = []
    image_uri = ""
    id_num = ""
    name = ""
    for i in range(1,total_count+2):
        url =f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&purposeName2={purposeName2}&nationalityName2={nationalityName2}&numOfRows=100&pageNo={i}'
        response = requests.get(url)
        response_dict = bs4.BeautifulSoup(response.content, 'html.parser')

        for data in response_dict.findAll('data'):
            for item in data.findAll('item'):
                if item['key'] == 'id':
                    id_num = item['value']
                elif item['key'] == 'nameKr':
                    name = item['value']
                elif item['key'] == 'imgUri':
                    image_uri = item['value']
            search_list.append([image_uri,id_num,name])

    return Response(search_list)