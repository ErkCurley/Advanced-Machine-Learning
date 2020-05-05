# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:35:25 2020

@author: EricC
"""

import requests
import json
import time

stop = False

while not stop:    
    f = open("pages.txt", "r")
    lastPage = 1
    for i in f.readlines():
        lastPage = i
    f.close()
    
    page = lastPage

    # tags = "Python"
    # tags = "R"
    # tags = "ggplot2;matplotlib"
    # tags = "ggplot2"
    # tags = "matplotlib"
    #tags = "Python;numpy"
    url = "https://api.stackexchange.com/2.2/questions?page={}&pagesize=75&order=asc&sort=creation&tagged={}&site=stackoverflow&key=JQJ5HqL9wHk3WQtdTVJGdw((".format(page,tags)
    print(url)

    response = requests.get(url)
    data = response.json()

    f = open("PlotQuestionsAll.txt","a")
    f.write(json.dumps(data))
    f.write("\n")
    f.close()
    
    time.sleep(1)
    
    if not data['has_more']:
        print("No more questions to read")
        stop = True
    
    if data['quota_remaining'] < 100:
        print("Max quota")
        break
    
    f = open("pages.txt","a")
    if data['has_more']:
        f.write(str(int(lastPage) + 1) + "\n")
    f.close()

