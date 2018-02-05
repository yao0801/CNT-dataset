f = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_trainval_img2xml.txt', 'r')
f_cl9_train = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_train_img2xml.txt', 'r')
f_cl9_val = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_val_img2xml.txt', 'r')
new_train = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_train_img2xm.txt', 'w')
new_val = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_val_img2xm.txt', 'w')
pre9_train = f_cl9_train.readlines()
pre9_val = f_cl9_val.readlines()
pre9_trainval =  f.readlines()
for i in pre9_train:
    if i in pre9_trainval:
        new_train.writelines(i)
for m in pre9_val:
    if m in pre9_trainval:
        new_val.writelines(m)
# print train
# for m in pre9_val:
#     val_name = m.strip('\n')
#     val.append(val_name)
# for l in f:
#     im_name = l.strip().split('.')[0]
#     im_name_1 = im_name.strip().split('/')[1]
#     print im_name_1
#     cur.append(im_name_1)
# for s in cur:
#     new_trainval.writelines(s + '\n')
# print len(cur)
# for line in train:
#     if line in cur:
#         new_train.writelines(line + '\n')
# for _ in val:
#     if _ in cur:
#         new_val.writelines(_ + '\n')
f.close()
f_cl9_train.close()
new_train.close()
f_cl9_val.close()
new_val.close()