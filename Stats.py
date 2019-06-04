#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:13:28 2019

@author: bxc583
"""

import scdb_linker
import p1
import Stats_Backend


path = r"/Users/bxc583/Downloads/Opinions/Data/data2" #change this variable to provide the path for the Harvard Data File

path_1 = r"/Users/bxc583/Downloads/Opinions/Data/SCDB_2018_02_justiceCentered_Citation.csv" #change this variable to provide the path for the SCDB Modern Data File
path_2 = r"/Users/bxc583/Downloads/Opinions/Data/SCDB_Legacy_04_justiceCentered_Citation.csv" #change this variable to provide the path for the SCDB Legacy Data File

harvard_dic_raw = p1.build_harvard_data(path)
print("\n")
(SCDB_dic,m_dic,l_dic,SCDB_year_dic) = scdb_linker.get_scdb_opinions(path_1,path_2)
 
print("--------------------------------------------------------------------------------")
print("Displaying Stats\n")
            
harvard_dic = Stats_Backend.create_Harvard_dic(harvard_dic_raw)

print("Getting Stats about Mismatched Cases......")
print('Total Cases in Harvard API: '+ str(len(harvard_dic)))

mismatch_cases = Stats_Backend.check_opinions_mismatch(harvard_dic,SCDB_dic,harvard_dic_raw)                 
       