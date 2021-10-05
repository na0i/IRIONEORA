import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import PCA
from pyspark.ml.feature import PCAModel

from scipy.spatial import distance

print('start')
spark = SparkSession\
        .builder\
        .master('spark://j5a601.p.ssafy.io:7077')\
        .appName('Search')\
        .getOrCreate()

model = PCAModel.load('./spark/model')
print(model)
print('end')