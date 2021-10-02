# Pyspark DataFrame에 맞게

import pandas 
import json

files = [
    '1to4000.json', '4000.json', '5000.json', '6000.json', '7000.json',
    '8000to12000.json', '12000to16000.json', '16000to20000.json', '20000to21000.json',
]


rawdata = []




with open('4000.json', 'r') as jason_file:
    jason_to_python = json.load(jason_file)

# print(jason_to_python)

face_item = {}
tmp = jason_to_python[0]

face_item['identification'] = list(tmp.keys())[0]


print(tmp)