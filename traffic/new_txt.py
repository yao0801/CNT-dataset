f = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_v2\ImageSets\clear\class_7/privshanxitraffic_class7_trainval.txt', 'r')
f_cl9_train = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_v2\ImageSets\clear\class_7/privshanxitraffic_class7_train.txt', 'r')
f_cl9_val = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_v2\ImageSets\clear\class_7/privshanxitraffic_class7_val.txt', 'r')
new_train = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_train_img2xml.txt', 'w')
new_val = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_val_img2xm.txt', 'w')
new_trainval = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_trainval_img2xm.txt', 'w')
pre9_train = f_cl9_train.readlines()
pre9_val = f_cl9_val.readlines()
pre9_trainval =  f.readlines()
for i in pre9_train:
    l = i.split('\n')[0]
    a = 'Images/' + l + '.jpg Annotations_7/' + l + '.xml\n'
    new_train.writelines(a)
for m in pre9_val:
    n = m.split('\n')[0]
    b = 'Images/' + n + '.jpg Annotations_7/' + n + '.xml\n'
    new_val.writelines(b)
for aa in pre9_trainval:
    vv = aa.split('\n')[0]
    nn = 'Images/' + vv + '.jpg Annotations_7/' + vv + '.xml\n'
    new_trainval.writelines(nn)
f.close()
f_cl9_train.close()
new_train.close()
f_cl9_val.close()
new_val.close()
new_trainval.close()

# for m in pre9_val:
#     if m in pre9_trainval:
#         new_val.writelines(m)