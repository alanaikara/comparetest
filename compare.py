#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:17:37 2019

@author: alan
"""
import csv
reader = csv.reader(open("person1.csv"))
person1 ={}
for row in reader:
    print(row)
    person1[row[0]]=row[1:]
    
    
reader = csv.reader(open("person2.csv"))
person2 ={}
for row in reader:
    print(row)
    if(len(row)>0):
        person2[row[0]]=row[1:]
        
#print(type(person2.get('ankle_left')))
#print(float(person2.get('knee_left')[0]))

#a=(list(person2.values()[2]['y']))
#print(float(list(person2.values())[2]['y']))

#first_key = list(person2.keys())[0]
#first_val = list(person2.values())[0]


def slopeF(skel_dict ,pos_1, pos_2):
    y1= float(skel_dict[pos_1][1])
    y2= float(skel_dict[pos_2][1])
    x1= float(skel_dict[pos_1][0])
    x2= float(skel_dict[pos_2][0])
    slope=(y2-y1)/(x2-x1)
    return slope

def calcslope(skelt_dict):
    slope_list=[]
    slope_list.append(slopeF(skelt_dict,'ankle_left','knee_left'))
    slope_list.append(slopeF(skelt_dict,'ankle_right','knee_right'))
    slope_list.append(slopeF(skelt_dict,'wrist_left','shoulder_left'))
    slope_list.append(slopeF(skelt_dict,'wrist_right','shoulder_right'))
    slope_list.append(slopeF(skelt_dict,'wrist_right','elbow_right'))
    slope_list.append(slopeF(skelt_dict,'wrist_left','elbow_left'))
    slope_list.append(slopeF(skelt_dict,'wrist_left','forehead'))
    slope_list.append(slopeF(skelt_dict,'wrist_right','forehead'))
    slope_list.append(slopeF(skelt_dict,'ankle_left','forehead'))
    slope_list.append(slopeF(skelt_dict,'ankle_right','forehead'))
    return(slope_list)

#calcslope(person1)
def compare(skelton1,skelton2,K):
    score=0;
    figure1 = calcslope(skelton1)
    figure2 = calcslope(skelton2)
    print(figure1)
    print(figure2)
    n=len(figure2)
    print(n)
    for x in range(0,n-1):
       a= abs(figure1[x])-abs(figure2[x])
       if(a<=5):
           score= score+10
           
    return score
compare(person1,person2,3)