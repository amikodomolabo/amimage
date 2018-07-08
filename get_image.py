#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

#api_key1 = "329523afc35a43ac8288c443c5afe938"
api_key1 = "b731af2b73f642b993cd874d878d571e"

#api_key2 = "d0569875d3cc4754883513439cfdeb3b"
api_key2 = "3f681b8799ca4c9b973bffb7aacd30ff"


def get_bing_image(query,offset=0,count = 150):
    url = 'https://api.cognitive.microsoft.com/bing/v7.0/images/search'
    headers = {'Ocp-Apim-Subscription-Key': api_key1,'Content-Type':'multipart/form-data'}
    res = requests.get(url,{'q':query,'count':count,'offset':offset,'filetype':'png'},headers=headers)
    res = json.loads(res.text)
    print(res)
    return res['value']

def save_image(filename, image):
    with open(filename, "wb") as fout:
        fout.write(image)

def get_item_image(query, fname_h, num):
    res = get_bing_image(query,0,num)
    num = 1
    urls = [i['contentUrl'] for i in res]
    for url in urls:
        try:
            image = requests.get(url).content
            save_image("./images/" + fname_h + str(num).zfill(4) + ".png", image)
            num += 1
        except:
            print("error")


get_item_image("ヤーコン","yacon",1000)
#get_item_image("たけのこ","takenoko",1000)
#get_item_image("メロン","melon",1000)
#get_item_image("すいか","suica",1000)
