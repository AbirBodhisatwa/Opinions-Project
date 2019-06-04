#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:29:08 2019

@author: bxc583
"""
import pandas as pd
import math

path_1 = r"/Users/bxc583/Downloads/Opinions/Data/SCDB_2018_02_justiceCentered_Citation.csv"
path_2 = r"/Users/bxc583/Downloads/Opinions/Data/SCDB_Legacy_04_justiceCentered_Citation.csv"

def build_supreme_court_data(path_1,path_2):
   
   print("Building Supreme Court Database Opinions List...\n")
   dataframe_modern = pd.read_csv(path_1,encoding='latin1')
   dataframe_legacy = pd.read_csv(path_2,encoding='latin1')

   modern_dic = {}
   legacy_dic = {}
   
   print("\nConstructing Modern Database Opinions List....")
   for i in range(len(dataframe_modern)):
      temp_lis = []
      key = dataframe_modern['caseId'][i]
    
      if key not in modern_dic:  
        modern_dic[key]= []
      
      temp_lis.append(dataframe_modern['decisionType'][i])
      temp_lis.append(dataframe_modern['usCite'][i])
      temp_lis.append(dataframe_modern['caseName'][i])
      temp_lis.append(dataframe_modern['justice'][i])
     
      
      op_val = dataframe_modern['opinion'][i]
    
      if math.isnan(op_val): 
          temp_lis.append(0)
      else:
          temp_lis.append(int(op_val))
        
      temp_lis.append(dataframe_modern['direction'][i])
      temp_lis.append(dataframe_modern['majority'][i])
      temp_lis.append(dataframe_modern['dateDecision'][i])
      
    
      modern_dic[key].append(temp_lis)
   
   print("Constructing Legacy Database Opinions List....") 
   for i in range(len(dataframe_legacy)):
      temp_lis = []
      key = dataframe_legacy['caseId'][i]
    
      if key not in legacy_dic:  
        legacy_dic[key]= []
      
      temp_lis.append(dataframe_legacy['decisionType'][i])
      temp_lis.append(dataframe_legacy['usCite'][i])
      temp_lis.append(dataframe_legacy['caseName'][i])
      temp_lis.append(dataframe_legacy['justice'][i])
     
      op_val = dataframe_legacy['opinion'][i]
    
      if math.isnan(op_val): 
          temp_lis.append(0)
      else:
          temp_lis.append(int(op_val))
        
      temp_lis.append(dataframe_legacy['direction'][i])
      temp_lis.append(dataframe_legacy['majority'][i])
      temp_lis.append(dataframe_legacy['dateDecision'][i])
    
      legacy_dic[key].append(temp_lis)
      
   return (modern_dic,legacy_dic) 
       
def count_opinions(case_dic,opinions_dic = {}):
    #opinions_dic = {}
    for case_id in case_dic:
        opinions_dic[case_dic[case_id][0][1]] = 0
        opinions = 0
        con = False
        for lis in case_dic[case_id]:
            if lis[4] == 2:
                opinions += 1
            elif lis[4] == 3:
                con = True
                
        opinions_dic[case_dic[case_id][0][1]] = opinions + int(con)
        
    return opinions_dic

def opinions_by_year(m_dic,l_dic):
    opinions_year = {}
    
    for s_id in m_dic.keys():
        if s_id[:4] not in opinions_year:
            opinions_year[s_id[:4]] = 0
        opinions_year[s_id[:4]] += 1
        
    for s_id in l_dic.keys():
        if s_id[:4] not in opinions_year:
            opinions_year[s_id[:4]] = 0
        opinions_year[s_id[:4]] += 1
        
    return opinions_year    
        
def get_scdb_opinions(path_1,path_2): 
   (modern_dic,legacy_dic) = build_supreme_court_data(path_1,path_2)
   print("Finalizing Opinions Count")
   opinion_dic = count_opinions(modern_dic)   
   #print(len(opinion_dic))
   opinion_dic = count_opinions(legacy_dic,opinion_dic)
   
   print("Collecting Some Vital Stats....")
   o_year_dict = opinions_by_year(modern_dic,legacy_dic)
   a = sorted(list(o_year_dict.keys()))
   
   print("Finished Building "+ str(sum(opinion_dic.values())) + " Opinions from Supreme Court Database for Years "+ str(a[0]) + "-" + str(a[-1]))  
   
   return (opinion_dic,modern_dic,legacy_dic,o_year_dict)

#(o_dic,m_dic,l_dic) = get_scdb_opinions(path_1,path_2)
#combined_opinion_dic = {**legacy_opinion_dic,**modern_opinion_dic}
#print(len(combined_opinion_dic))
