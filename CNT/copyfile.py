# -*- coding:utf-8 -*-
import os
import shutil
import random

f = open('C:\Users\priv_data2\Desktop\crack.txt', 'r')
crack_list = f.readlines()
all_list = os.listdir("E:\crack_xxs\\1225\cam5")
new_list = []
res = []
for name in crack_list:
    c_name = name.split('\n')[0]
    new_list.append(c_name)
for img in all_list:
    if img not in new_list:
        res.append(img)
for rdm in random.sample([i for i in range(len(res))], 500):
    oldname = "E:\crack_xxs\\1225\cam5\\" + res[rdm]
    newname = "C:\Users\priv_data2\Desktop\\no_crack\\" + res[rdm]
    shutil.copyfile(oldname, newname)
