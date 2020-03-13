#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:30:04 2020

@author: godson
"""

import pandas as pd
import re

df = pd.read_csv("articlesByCategories.csv")
print(df.columns)
contents = df["Content"]


filename = "articleskabye.txt"

articleWithContent = 0

with open(filename, 'a') as out:
    for index, row in df.iterrows() :
        if len(str(row["Content"])) > 5 and not ("Modèle" in row["title"]):#Only articles having actual readable content
            #Keeping count of how many articles are not empty
            articleWithContent = articleWithContent + 1
            #Categories
            catRaw = row["category"]
            catList = catRaw.split(",")
            catString = ""
            for idx,  cat in enumerate(catList) :
                catString = catString + cat.split(":")[1]  #We are only interested in the name of the category
                if (idx < len(catList) - 1):
                    catString = catString + ", "
                    
            catString = catString.replace("'","").replace("]","").replace("!","")
            print(catString)
            #Content
            sentences = row["Content"].split(".")
            for sentence in sentences :
                if(not ("==" in sentence) and sentence.strip()):
                    sentence = sentence.replace("\n"," ").strip("\n")
                    out.write("\t\t"+sentence+".\n")
            out.write("Wikipedia"+"\t\t"+row["title"]+"\t\t"+row["Url"]+"\t\t"+catString+"\n")
            
