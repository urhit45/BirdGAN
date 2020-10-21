# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:38:27 2020

@author: Rohit
"""

import os
import shutil

source = "C:\\Users\\Rohit\\Desktop\\consolidated"
destination = "C:\\Users\\Rohit\\Desktop\\consolidated\\CODE\\images"

directory = os.fsencode(source)
count = 1
for file in os.listdir(directory):
    folder = source+"\\"+ os.fsdecode(file)
    for image in os.listdir(folder):
         filename = os.fsdecode(image)
         #print(filename)
         if filename.endswith(".jpg") or filename.endswith(".jpeg"): 
             # print(os.path.join(directory, filename))
             shutil.move(folder+"\\"+filename, destination+"\\"+str(count)+".jpg")
             count += 1
             continue
         else:
             continue