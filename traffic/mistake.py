f = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_trainval_img2xml.txt', 'r')
f_cl9_train = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_train_img2xml.txt', 'r')
f_cl9_val = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_val_img2xml.txt', 'r')
# new_train = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_train_img2xml.txt', 'w')
# new_val = open('C:\Users\priv_data2\Desktop/privshanxitraffic_class9_val_img2xm.txt', 'w')
pre9_train = f_cl9_train.readlines()
pre9_val = f_cl9_val.readlines()
pre9_trainval =  f.readlines()
for i in pre9_train:
    if i not in pre9_trainval:
        # print i
        pass
    if not i.endswith('\n'):
        print 'jjjjjjj', i
for m in pre9_val:
    if m not in pre9_trainval:
        # print m
        pass
    if not m.endswith('\n'):
        print 'mmmmmmmmmm', m