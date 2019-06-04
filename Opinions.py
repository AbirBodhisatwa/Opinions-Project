# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:10:00 2018

@author: Bodhisatwa
"""

class opinions:
  def __init__(self, case_id, o_type, author, text,current_cit,year,o_id):
      self.case_id = case_id
      self.o_type = o_type
      self.author = author
      self.text = text
      self.current_cit = current_cit
      self.year = year
      self.other_cites = []
      self.o_id = o_id
  #def get_citing_case(self):
      #self.citing_case = p1.citations[self.case_id]
  def get_current_citation(self):
      return self.current_cit
  def get_author(self):
      return self.author
  def p(self):
      print(str(self.o_id) + " " + str(self.case_id) + " "+self.o_type + " "+ self.author + " "+ self.current_cit)
      print(self.other_cites)
      
  #def make_unigrams(self)    
      
      
      
#Universal City Studios, Inc. v. Corley, 273 F.3d at 435
#
#Corley, 273 F.3d at 435
#
#273 F.3d at 435
#
#Id. at 435      
      
      