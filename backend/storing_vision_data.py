# 유물 사진 URL을 넣어서 vision API에 적용해보자!
# CSV 파일로 만들 것!
from get_vision_data import *

IMAGE_URL = 'emuseum.go.kr/openapi/img?serviceKey=Qhwj%2B5KHmC8OENHvRm3La%2FxMxbXlXv7HD6Zkm8mpG%2Fg%2BiVN%2BGffbevfZoVDr9vDzsHjkpwtUkmEh1N%2BjnKKKPWf5FfRhBAYcOLum5fp5Wyjs8C%2FCR%2FHztEnDm%2FjtSOw5v%2FBVwBaOcAw%3D&imageId=ZUdWVk93RzZrbGEzZE9RMHBBU0FvL210c2s0ck5Id2swSnBTenhTV1dwM1k1QW9UcXYwYXdIWEJWMkllUjdwY05rMEZIb25CeVdrQ3RSK1BMM1JGN1g3SS9Ja2YrZURF'

data = get_vision_data(IMAGE_URL)
print( data )