# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 08:15:53 2018

@author: Bodhisatwa
"""
import Opinions
#import csv
import re
           
r1 = re.compile("(\d){1,4}(\s)+U.(\s)*S.(\s)+(\d){1,4}")    
#r2 = re.compile(r"(\d){1,4}(\s)+U.S.(\s)+\(Black\)(\s)+(\d){1,4}")


def get_citations(obj_dic):
    c = 0
    for year in obj_dic:
      for o in obj_dic[year]:
        #o.p()
        #print(o.text)
        for i in re.finditer(r1,o.text):
            o.other_cites.append(i.group())
        if len(o.other_cites) > 0: 
           #print(o.other_cites)
           pass
        else:
            #print("No citations found in object body "+o.current_cit)
            c += 1
    #print(len(o_obj))
    #print(c)       
def get_opinion_id(obj_dic,citation,cyear):
    a = []
    for year in obj_dic:
        if year <= cyear:
            for o in obj_dic[year]:
                if o.current_cit == citation:
                    a.append(o)
    if len(a) == 1:
       return a[0].o_id
    elif len(a) > 1:
       for o in a:
           if o.o_type == 'majority':
               return o.o_id
    else:
        return 0
   

def write_data(o_obj):
    pass    