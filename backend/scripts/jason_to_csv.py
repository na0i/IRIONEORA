# Pyspark DataFrame에 맞게

import pandas 
import json

files = [
    '1to4000.json', '4000.json', '5000.json', '6000.json', '7000.json',
    '8000to12000.json', '12000to16000.json', '16000to20000.json', '20000to21000.json',
]

with open('4000.json', 'r', encoding="utf-8", newline="") as '4000.json', \
    