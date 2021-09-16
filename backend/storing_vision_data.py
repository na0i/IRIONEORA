# 유물 사진 URL을 넣어서 vision API에 적용해보자!
# CSV 파일로 만들 것!

import requests

IMAGE_URL = 'https://emuseum.go.kr/openapi/img?serviceKey=CGlBMoJxMaPqI9InypnTeJr%2FNYurz%2FWIFV%2FelT3gmeubzSCWLaaZIyC1j9Nb0Gq2TFg8U4akJMRftUTpwwFElit8BnY1rqPOl8n6SHQbmu2%2B7pbw1RAFUvph4fbRXnhKMB9wbTkkNe8%3D&imageId=WVBzbjFFcU5iUWlhU0dxRFlMYUZxL2FKbHJxTlk1VGJ0dGdmK1VwbDNCRnlOdFBSRGNubWJnMGRrTUN4aFY3UWliVjJKM2s5VWN3Q1NpdENEZEdUb2ZqeHdXakVVUENq'
KEY=

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'

headers = {}
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['Authorization'] = 'KakaoAK ' + KEY

data = { 'image_url':IMAGE_URL }

res = requests.post( API_URL, headers=headers, data=data )

if res.status_code == 200:
    print('success')
    print(res.text)
else:
    print(F'Fail {res.status_code}')