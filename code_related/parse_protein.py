# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:51:08 2016

@author: yuyue
"""

file = open('protein_sequence_raw.txt','r')
alldata = file.read()
file.close()
newfile = open('protein_sequence.txt','w')
newdata=[]
splitdata = alldata.split('\n')
for line in splitdata:
    if len(line)>0 and line[0] != '>':
        newdata.append(line)
joineddata = '\n'.join(newdata)
newfile.write(joineddata)
newfile.close()
        