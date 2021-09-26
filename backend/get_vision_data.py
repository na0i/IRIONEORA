import requests
from io import BytesIO

def get_image_from_url(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.content
        print( f'fail to get image. code({res.status_code})')
    except:
        print(url)
        print( 'exception raised to get image')
    return None

def get_face_data(image):
    API_KEY= '67852745621896a093fa2abcffbd1275'
    API_URL = 'https://dapi.kakao.com/v2/vision/face/detect'

    headers = { 'Authorization': 'KakaoAK ' + API_KEY }
    files = { 'image': ('image.jpg', BytesIO(image))}

    try:
        res = requests.post( API_URL, headers=headers, files=files)
        if res.status_code == 200:
            return res.json()
        print( f'fail to get face data. code({res.status_code})')
    except:
        print( 'exception raised to get face data')


def get_vision_data(url):
    if url.startswith('https://') == False:
        url = 'https://' + url
    
    image = get_image_from_url(url)

    return get_face_data(image)