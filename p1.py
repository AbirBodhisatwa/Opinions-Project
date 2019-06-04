#-*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:43:43 2018

@author: Bodhisatwa
"""
import json
import re
import p2
import Opinions

#global variable for counting the number of opinions and assigning each opinions a number
o_id = 0

#function which constructs the opinion objects for the entire Harvard Dataset
def build_harvard_data(path):
  #dictionary to store the opinions of cases, grouped by year(keys).  
  o_dic = {}
  #o_id = 0
  print("Building Harvard API Data Case Opinion Objects....")

  def make_opinions(cid,re_obj,authors,texts,cite,year):
      o_type = []
      for s in re_obj:
       if 'majority' in s:
          o_type.append('majority') 
       if 'concurrence' in s:
          o_type.append('concurrence')    
       if 'dissent' in s:
          o_type.append('dissent')
        
      #syl_body = texts[0]  #syllabus body
      texts.pop(0)
    
      for i in range(len(o_type)): 
         if len(o_type) == len(authors):
           global o_id
           o_id += 1
           o = Opinions.opinions(cid,o_type[i],authors[i],texts[i],cite,year,o_id) 
           #o.get_citing_case()
           try:  
             o_dic[year].append(o)
           except KeyError:
             o_dic[year] = []
             o_dic[year].append(o)
           #o.p()
         else:
             pass
             #print('No of opinions does not match the no. of authors')
             #print(o_type)
             #print(authors)
             #print(cid)       

  dic = [] #local dictionary to store the parsed json file
  print("Reading Harvard Json File....")
  a = open(path,'r') #file pointer for opening json file

  #loading the json data to the local dictionary
  for line in a:
      parsed_json = json.loads(line)
      dic.append(parsed_json)
    
  #case dictionary to store the case_id as key and case_body as values    
  case = {}
  citations = {}
  decision_year = {}
  #initializaing the case dictionary to
  for d in dic:   
      for k in d:
          #print(k)
          if k == "casebody":
             case[d["id"]] = d[k]["data"]
          elif k == "citations":
              citations[d["id"]] = d[k][0]["cite"]
          elif k == "decision_date":
              decision_year[d["id"]] = d["decision_date"][:4]
              #print(d["decision_date"][:4])
         
  #print(citations)
  print("Constructing Harvard Opinion Objects....")
  for cid in case:
         obj = re.findall(r'<opinion type=\"\w+\">',case[cid]) # searching for opinion
         obj2 = re.findall(r'\w+.</author>',case[cid]) # searching for authors
         authors = []
         for a in obj2:
             i = a.find('.')
             authors.append(a[:i])
         indices = [m.start() for m in re.finditer('<opinion type=', case[cid])]
         break_points = []
         break_points.append(0)
         for i in indices:
             break_points.append(i)
         break_points.append(len(case[cid]))
         texts = []
         for i in range(len(break_points)-1):
             texts.append(case[cid][break_points[i]:break_points[i+1]-1])
           
         make_opinions(cid,obj,authors,texts,citations[cid],decision_year[cid])
         #print(cid)
  print("Finalizing Case Citations....")     
  p2.get_citations(o_dic)
  print("Collecting Some Vital Stats....")
  a = sorted(list(o_dic.keys()))
  print("Finished Building "+ str(o_id) + " Opinion Objects from Harvard API for Years "+ str(a[0]) + "-" + str(a[-1]))
  return o_dic

#path = r"/Users/bxc583/Downloads/Opinions/Data/data2" #change this variable to provide the path for the Harvard Data File

#harvard_dic = build_harvard_data(path)
#n = 0   #local variable to count the total number of opinions
#
#for y in harvard_dic:
#    n += len(harvard_dic[y])
#
#print(n)
#    for o in harvard_dic[y]:
#        o.p()




       