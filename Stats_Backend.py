#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:35:42 2019

@author: bxc583
"""
import os

def yearly_stats(harvard_dic_raw,SCDB_year_dic):
   for year in harvard_dic_raw:
       print("In the Year "+ str(int(year))+ " : Harvard API has "+ str(len(harvard_dic_raw[year]))+ " Opinions and SCDB has " + str(SCDB_year_dic[year])+ " Opinions")

def create_Harvard_dic(harvard_dic_raw):
    harvard_dic = {}
    for year in harvard_dic_raw:
       for op_obj in harvard_dic_raw[year]:
           cite = op_obj.get_current_citation()
           if cite not in harvard_dic:
               harvard_dic[cite] = 0
           harvard_dic[cite] += 1
    return harvard_dic       
  
def check_opinions_mismatch(harvard_dic,SCDB_dic,harvard_dic_raw):
    mismatched_cases = []
    curr_dir = os.getcwd()
    mismatch_path = curr_dir + '/mismatch_cases.txt'
    missing_path = curr_dir + '/missing_cases.txt'
    
    f1 = open(mismatch_path,'w')
    f2 = open(missing_path,'w')
    ms = 0
    
    for cite in harvard_dic.keys():
      try:
          if (int(harvard_dic[cite]) != int(SCDB_dic[cite])): 
             mismatched_cases.append(cite)
      except KeyError:
                 s = 'Case '+ cite + ' missing in Supreme Court Database\n'
                 f2.write(s)
                 ms += 1
                 
    print('\nChecking for Percuriam Opinons....')
    mismatched_cases = check_percuriam_opinions(mismatched_cases,harvard_dic_raw)      
    
    for cite in mismatched_cases:
        s = "For US Cite: "+ cite + " Harvard Opinions: " + str(harvard_dic[cite]) + " SCDB Opinions: "+ str(SCDB_dic[cite]) + '\n'
        f1.write(s)
        
    print('Total Mismatched Cases: '+ str(len(mismatched_cases)))
    print('Total Missing Cases in Supreme Court Database: '+ str(ms))             
    print("\nInfo File for Mismatched Cases Written at: "+ mismatch_path)
    print("Info File for Missing Cases Written at: "+ missing_path)
              
    return mismatched_cases

def check_percuriam_opinions(mismatched_cases,harvard_dic_raw):
    curr_dir = os.getcwd()
    mismatched_info_path = curr_dir + '/mismatch_cases_info.txt'
    f = open(mismatched_info_path,'w')
    
    percuriam_cases = []
    for cite in mismatched_cases:
        obj_lis = get_opinion_obj_by_citation(harvard_dic_raw,cite)
        for opinion_obj in obj_lis:
            opinion_author = opinion_obj.get_author()
            if 'curiam' in opinion_author.lower():
                percuriam_cases.append(cite)
            else:
                s = "Author for Mismatched Case "+ cite + " is "+ opinion_author + "\n"
                s = s.encode('utf-8')
                f.write(s)
            
    print('Total Percuriam Opinion Cases: '+ str(len(percuriam_cases)))
    refined_mismatch = list(set(mismatched_cases) - set(percuriam_cases))
    return refined_mismatch 

def get_opinion_obj_by_citation(harvard_dic_raw,cite):
    objs = []
    for year in harvard_dic_raw:
        for obj in harvard_dic_raw[year]:
            if cite == obj.get_current_citation():
                objs.apppend(obj)
    if len(objs) == 0:            
       return None
    return objs        

 