import json

import requests, bs4
import xmltodict
import pprint

import xml.etree.ElementTree as ET

URL = 'http://www.emuseum.go.kr/openapi/relic/list'
API_KEY = 'SrLLfGdZjGbS5OmPmSlewYvcR6tXPmpk11SduYlvFr7r6CA7L9vjF7JRSx7rhrTEvOdAlUDtqkY9HJAg8+Y6ww=='

''' 
serviceKey = 인증키 
numOfRows = 한 페이지 결과 수 -> 기본값 10
pageNo = 페이지 번호 
'''

page = 1
params = {'serviceKey': API_KEY, 'numOfRows': 100, 'pageNo': page}

# 유물리스트
artifacts = []

for i in range(1, 10000 // 100 + 2):
    params['pageNo'] = i
    r = requests.get(URL, params=params)

    xml_data = bs4.BeautifulSoup(r.content, 'html.parser')

    for data in xml_data.findAll('data'):
        single = dict()
        items = data.findAll('item')
        for item in items:
            if item['key'] == 'id':
                single[item['key']] = item['value']

            elif item['key'] == 'imgUri':
                single[item['key']] = item['value']

        artifacts.append(single)


    print(len(artifacts))

# json_data = json.dumps(artifacts)
with open('./artifact_list.json', 'w') as outfile:
    json.dump(artifacts, outfile)








