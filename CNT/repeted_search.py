# -*- coding:utf-8 -*-
import os
import shutil

f = open('C:\Users\priv_data2\Desktop\cl.txt', 'r')
crack_list = f.readlines()
all_list = os.listdir("E:\Priv_crack_v02\\n")
new_list = []
for name in crack_list:
    c_name = name.split(' ')[0]
    new_list.append(c_name)
for img in all_list:
    if img in new_list:
        oldname = "E:\Priv_crack_v02\\n\\" + img
        newname = "C:\Users\priv_data2\Desktop\\n_test\\" + img
        shutil.copyfile(oldname, newname)