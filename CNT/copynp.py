# -*- coding:utf-8 -*-
import os
import shutil
import random
p_train = os.listdir("C:\Users\priv_data2\Desktop\\no")
# f = open('C:\Users\priv_data2\Desktop\cp.txt', 'r')
# crack_list = f.readlines()
# new_list = []
# for name in crack_list:
#     c_name = name.split(' ')[0]
#     new_list.append(c_name)
for rdm in random.sample([i for i in range(len(p_train))],15000):
# for i in p_train:
#     if i in new_list:
    oldname = "C:\Users\priv_data2\Desktop\\no\\" + p_train[rdm]
    newname = "E:\CNT_v0.2.2\\n_test\\" + p_train[rdm]
    shutil.copyfile(oldname,newname)


# f = open('C:\Users\priv_data2\Desktop\crack.txt', 'r')
# crack_list = f.readlines()
# all_list = os.listdir("E:\crack_xxs\\1225\cam7")
# new_list = []
# for name in crack_list:
#     c_name = name.split('\n')[0]
#     new_list.append(c_name)
# for img in all_list:
#     if img not in new_list:
#         oldname = "E:\crack_xxs\\1225\cam7\\" + img
#         newname = "C:\Users\priv_data2\Desktop\\no\\" + img
#         shutil.copyfile(oldname, newname)