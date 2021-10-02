from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from artifacts.models import Artifact
# from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

# from pyspark.sql import SparkSession

# spark = SparkSession\
#         .builder\
#         .master('spark://127.0.0.1:7077')\
#         .appName('Python Spark SQL basic example')\
#         .getOrCreate()

# def index(request):
#     sc = spark.sparkContext

#     # json 파일 읽어들이기
#     test = spark.read.json('/home/path/test.json')

#     # printSchema()로 json파일의 스키마 형태 볼수 있음
#     test.printSchema()
#     return render(request, 'test.html')
# Create your views here.



def test(request):
    return 'just test'



# 유저 얼굴 데이터 받아와서 닮은 얼굴 뿌리기
@api_view(['POST'])
def user_face(request):
    print(request.data)

    dummydata = [
        {'identification': 'PS0100100102102727900000','name': '이건첫번째야', 'width': 3000, 'height': 2000, 'x': 0.4754312744140625, 'y': 0.6482667846679687, 'w': 0.05687882486979168, 'h': 0.08531817626953131},
        {'identification': 'PS0100100100900173100000','name': '이건두번째고', 'width': 669, 'height': 515, 'x': 0.43930195122734494, 'y': 0.11844135765890473, 'w': 0.08157868663291756, 'h': 0.10597306038569479},
        # 같은 그림에 두 얼굴
        {'identification': 'PS0100100100900260500000', 'name': '아이스크림이', 'width': 1592, 'height': 3000, 'x': 0.6141179913851484, 'y': 0.5116527506510417, 'w': 0.08356299472214579, 'h': 0.044344075520833304},        
        {'identification': 'PS0100100100900260500000', 'name': '먹고싶어', 'width': 1592, 'height': 3000, 'x': 0.3875239003243758, 'y': 0.6396309000651041, 'w': 0.06894641665358042, 'h': 0.036587605794270894},
    ]

    for i in range(len(dummydata)):
        artifact_id = dummydata[i]['identification']
        artifact = get_object_or_404(Artifact, identification_number=artifact_id)
        # print(artifact.image_uri)
        dummydata[i]['url'] = artifact.image_uri
        # dummydata[i]['name'] = artifact.name

    return Response(dummydata)
    # return HttpResponse(200)