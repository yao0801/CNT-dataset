f = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_trainval_img2xml.txt', 'r')
f_cl9_train = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_train.txt', 'r')
f_cl9_val = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_val.txt', 'r')
new_train = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_train.txt', 'w')
new_val = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_val.txt', 'w')
new_trainval = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_trainval.txt', 'w')
pre9_train = f_cl9_train.readlines()
pre9_val = f_cl9_val.readlines()
cur = []
train = []
val = []
for i in pre9_train:
    train_name = i.strip('\n')
    train.append(train_name)
print len(set(train))
for m in pre9_val:
    val_name = m.strip('\n')
    val.append(val_name)
print len(set(val))
for l in f:
    im_name = l.strip().split('.')[0]
    im_name_1 = im_name.strip().split('/')[1]
    cur.append(im_name_1)
print len(set(cur))
for s in cur:
    new_trainval.writelines(s + '\n')
for line in train:
    if line in cur:
        new_train.writelines(line + '\n')
for _ in val:
    if _ in cur:
        new_val.writelines(_ + '\n')
f.close()
f_cl9_train.close()
new_train.close()
f_cl9_val.close()
new_val.close()
