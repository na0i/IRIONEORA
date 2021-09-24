from django.shortcuts import render, get_object_or_404

from .models import Artifact
from .serializers import ArtifactSerializer, ArtifactLikeSerializer, ArtifactResembleSerializer

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from urllib.request import urlopen
import json
import csv
import requests
import bs4
import xmltodict

# 저장 여부 확인
def is_saved(id):
    if not Artifact.objects.all().filter(identification_number=id):
        return False


# db에 저장
def save_to_db(data):
    serializer = ArtifactSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()


def get_csv():
    # 소장품 상세정보 불러오기
    URL = 'http://www.emuseum.go.kr/openapi/relic/detail'
    API_KEY = 'SrLLfGdZjGbS5OmPmSlewYvcR6tXPmpk11SduYlvFr7r6CA7L9vjF7JRSx7rhrTEvOdAlUDtqkY9HJAg8+Y6ww=='

    with open('./국립중앙박물관_전국 박물관 유물정보_20190920..csv', encoding='cp949') as f:
        data = csv.reader(f)
        for line in data:
            if line[5] == '문화예술' or line[5] == '종교신앙':
                id = line[0]
                if not Artifact.objects.all().filter(identification_number=id):
                    params = {'serviceKey': API_KEY, 'id': id}

                    r = requests.get(URL, params=params)

                    xml_data = bs4.BeautifulSoup(r.content, 'html.parser')

                    print(xml_data)
                    for item in xml_data.findAll('item'):
                        if item['key'] == 'imgUri':
                            image_uri = item['value']

                    data = {
                        'identification_number': id,
                        'image_uri': image_uri
                    }

                    serializer = ArtifactSerializer(data=data)

                    if serializer.is_valid(raise_exception=True):
                        serializer.save()

                    break


service_key = 'SqZskQNLBydKAJrTV5fUn3zRuenH7ELym5KvJWma15ABpxIYBeQK15yeq+cLDfiGBiMv8Pt5VFk1H0Sz4lX3yw=='

# 유물 상세정보
@api_view(['GET'])
def artifact_detail(request, artifact_id):
    
    # 유물 상세 정보 가져오기
    artifact_url = f"http://www.emuseum.go.kr/openapi/relic/detail?serviceKey={service_key}&id={artifact_id}"
    url_open = urlopen(artifact_url)
    response_xml = url_open.read().decode('utf-8')
    response_dict = xmltodict.parse(response_xml)
    response_json = json.dumps(response_dict)

    #수정 vue에 필요한 응답을 만들기
    return Response(response_json)


# 유물 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def artifact_like(request, artifact_pk):
    artifact = get_object_or_404(Artifact, pk=artifact_pk)
    user = request.user

    # username: column name
    # user: user 객체(비로그인시 anonymous)
    # 알아서 찾아서 넣어주는듯..?
    if artifact.like_users.filter(username=user).exists():
        artifact.like_users.remove(user)
    
    else:
        artifact.like_users.add(user)
    
    serializer = ArtifactLikeSerializer(artifact)
    return Response(serializer.data)


# 닮은 유물 저장
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def artifact_resemble(request, artifact_pk):
    artifact = get_object_or_404(Artifact, pk=artifact_pk)
    user = request.user

    if artifact.resemble_users.filter(username=user).exists():
        pass
    
    else:
        artifact.resemble_users.add(user)
    
    serializer = ArtifactResembleSerializer(artifact)
    return Response(serializer.data)
