# 유물 사진 URL을 넣어서 vision API에 적용해보자!
# CSV 파일로 만들 것!
import requests
from io import BytesIO

#IMAGE_URL = 'https://emuseum.go.kr/openapi/img?serviceKey=Qhwj%2B5KHmC8OENHvRm3La%2FxMxbXlXv7HD6Zkm8mpG%2Fg%2BiVN%2BGffbevfZoVDr9vDzsHjkpwtUkmEh1N%2BjnKKKPWf5FfRhBAYcOLum5fp5Wyjs8C%2FCR%2FHztEnDm%2FjtSOw5v%2FBVwBaOcAw%3D&imageId=ZUdWVk93RzZrbGEzZE9RMHBBU0FvL210c2s0ck5Id2swSnBTenhTV1dwM1k1QW9UcXYwYXdIWEJWMkllUjdwY05rMEZIb25CeVdrQ3RSK1BMM1JGN1g3SS9Ja2YrZURF'
#IMAGE_URL = 'https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/01.jpg'
KEY= '3ea7603f345b5f0e692c85f233e79d02'

API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'

def face_detect():
    headers = {}
    headers['Authorization'] = 'KakaoAK ' + KEY

    print(headers)
    files = {'image': ('test.jpg', open('test.jpg','rb')) }

    res = requests.post( API_URL, headers=headers, files=files )
    if res.status_code == 200:
        print('success')
        print(res.text)
    else:
        print(F'Fail {res.status_code}')
        print(res.text)

def get_image(url):
    res = requests.get(url)
    if res.status_code == 200:
        with open('test.jpg', 'wb') as f:
            f.write(res.content)
            f.flush()
            f.close()

#get_image(IMAGE_URL)
#rint(img)
face_detect()
