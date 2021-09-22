from django.shortcuts import render

from .models import Artifact
from .serializers import ArtifactSerializer

import csv
import requests
import bs4


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