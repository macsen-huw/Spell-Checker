# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:22:02 2023

@author: macse
"""
 
#Read the file and iterate between every sentence
for piece in open("Corpws Cymraeg.txt", encoding="utf-8").read().split("\n"):
      #Remove any unwanted characters e.g Emojis and punctuation (full stops, question marks, etc)
      sentence = ''.join(c for c in piece if c.isalpha() or c == "'" or c == "’" or  c == "‘" or c == " " or c == "-")
      
      #Write cleaned sentences to new file
      f = open("corpus.txt", "a", encoding="utf-8")
      f.write(sentence + "\n")
      
      f.close()
