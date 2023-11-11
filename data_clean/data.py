# -*- coding: utf-8 -*-

import requests

def playground():
    response = requests.get('https://data.taipei/api/v1/dataset/c7784a9f-e11e-4145-8b72-95b44fdc7b83?scope=resourceAquire&limit=1000')  # &limit=1000 
    allData = response.json()['result']['results']

    countData = {}
    for i in allData:
        district = i['district']
        if district not in countData:
            countData[district] = 1
        else:
            countData[district] += 1
    
    finalData = {
        "data": [
            {
                "name": "",
                "data": [{"x": i, "y": count} for i, count in countData.items()]
            }
        ]
    }
    return finalData


def disability():
    response = requests.get('https://data.taipei/api/v1/dataset/f26a4c04-771f-42f3-a028-1a7e89303509?scope=resourceAquire')
    allData = response.json()['result']['results']
    
    for i in range(len(allData)):
        if allData[i]['address'][2]=="台北":
            allData[i]['address'][2]="臺北"
            
    return allData


# finalData = {
#     "data": [
#         {
#             "name": "",
#             }
#     ]
# }