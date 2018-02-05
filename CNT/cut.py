# -*- coding:utf-8 -*-
import os
import cv2
import random
crack_root = "C:\Users\priv_data2\Desktop\\no_crack"
all_list = os.listdir("C:\Users\priv_data2\Desktop\\no_crack")
save_root = "C:\Users\priv_data2\Desktop\\no"
for file in all_list:
    pre_dir = os.path.join(crack_root, file)
    img = cv2.imread(pre_dir)
    cut_list = []
    final_list = []
    for i in xrange(8):
        for j in xrange(8):
            cut_imgs = img[512*i : 512*(i + 1),512 * j : 512*(j + 1)]
            cut_list.append(cut_imgs)
    for rdm in random.sample([i for i in range(63)],10):
        final_list.append(cut_list[rdm])
        for x in final_list:
        # rdm += 1
            stri = '_' + str(rdm) + '.png'
            final_root = os.path.join(save_root, file.replace('.png', stri))
            cv2.imwrite(final_root, x)

                # print rdm
                # for _ in range(10):
                # stri = '_'+ str(count)+'.png'
                # proot = os.path.join(save_p_root, file.replace('.png', stri))
