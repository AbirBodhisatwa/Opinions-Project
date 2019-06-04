# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:44:21 2019

@author: Bodhisatwa
"""

#import csv
import pandas as pd

file_path = r'D:\PSU_Parser\SCDB_2018_02_justiceCentered_Citation.csv'

data = pd.read_csv(file_path,encoding = 'latin1')

dic = {}
for i in range(len(data)):
    key = data['caseId'][i]
    dic[key]= []
    dic[key].append(data['decisionType'][i])
    dic[key].append(data['usCite'][i])
    dic[key].append(data['caseName'][i])
    dic[key].append(data['justice'][i])
    dic[key].append(data['opinion'][i])
    dic[key].append(data['direction'][i])
    dic[key].append(data['majority'][i])

