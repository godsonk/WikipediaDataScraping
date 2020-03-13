#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:30:04 2020

@author: godson
"""

import pandas as pd

df = pd.read_csv("articlesEwe.csv")
print(df.columns)

filename = "articlesewe.txt"

articleWithContent = 0

with open(filename, 'a') as out:
    for index, row in df.iterrows() :
        if len(str(row["Content"])) > 5 and not ("Modèle" in row["title"]):#Only articles having actual readable content
            #Keeping count of how many articles are not empty
            articleWithContent = articleWithContent + 1
            #Content
            sentences = row["Content"].split(".")
            for sentence in sentences :
                if(sentence.strip()):
                    sentence = sentence.replace("\n"," ").strip().strip("==")
                    out.write("\t\t"+sentence+".\n")
            out.write("Wikipedia"+"\t\t"+row["title"]+"\t\t"+row["Url"]+"\t\tArticle\n")
            
        
