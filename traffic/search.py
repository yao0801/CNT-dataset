# -*- coding: utf-8 -*-
import os

path = 'C:\Users\priv_data2\Desktop\\aa\Priv_shanxitraffic_v2\Images'
list_name = []
f = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_v2\ImageSets\clear\class_7/privshanxitraffic_class7_trainval.txt', 'r')
pre9_trainval =  f.readlines()
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    name = file_path.split('\\')[7].split('.')[0]
    list_name.append(name + '\n')
c = 0
for i in list_name:
    if i not in pre9_trainval:
        c +=1
        print i
# print list_name
print c
# print pre9_trainval