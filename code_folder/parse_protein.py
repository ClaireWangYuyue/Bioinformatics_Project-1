# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:51:08 2016

@author: yuyue
"""
# change file and newfile to different files to parse protein of different species

file = open('protein_sequence_raw.txt','r')
# file = open('AP008971_protein.txt','r')
# file = open('CP000724_protein.txt','r')
# file = open('CP002390_protein.txt','r')
# file = open('CP002987_protein.txt','r')

alldata = file.read()
file.close()
newfile = open('protein_sequence.txt','w')
# file = open('parsed_AP008971_protein.txt','r')
# file = open('parsed_CP000724_protein.txt','r')
# file = open('parsed_CP002390_protein.txt','r')
# file = open('parsed_CP002987_protein.txt','r')

newdata=[]
splitdata = alldata.split('\n')
for line in splitdata:
    if len(line)>0 and line[0] != '>':
        newdata.append(line)
joineddata = '\n'.join(newdata)
newfile.write(joineddata)
newfile.close()
        
