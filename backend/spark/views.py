from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .master('spark://127.0.0.1:7077')\
        .appName('Python Spark SQL basic example')\
        .getOrCreate()

def index(request):
    sc = spark.sparkContext

    # json 파일 읽어들이기
    test = spark.read.json('/home/path/test.json')

    # printSchema()로 json파일의 스키마 형태 볼수 있음
    test.printSchema()
    return render(request, 'test.html')
# Create your views here.



def test(request):
    return 'just test'



# 유저 얼굴 데이터 받아와서 닮은 얼굴 뿌리기
@api_view(['POST'])
def user_face(request):
    print(request.data)

    return HttpResponse(200)