import os
import random
# p_train = os.listdir("E:\CNT_v0.2.2\p_train")
p_test = os.listdir("E:\CNT_v0.2.2\p_test")
# n_val = os.listdir("E:\CNT_v0.2.2\\n_val")
n_test = os.listdir("E:\CNT_v0.2.2\\n_test")
# n_train = os.listdir("E:\CNT_v0.2.2\\n_train")
# new_train = open('E:\CNT_v0.2.2\\train.txt', 'w')
# new_val = open('E:\CNT_v0.2.2\\val.txt', 'w')
new_test = open('E:\CNT_v0.2.2\\test.txt', 'w')
# train_list = []
# val_list = []
test_list = []
# for l in p_train:
#     ll = l + ' 0'+'\n'
#     train_list.append(ll)
# for v in n_train:
#     vv = v + ' 1'+'\n'
#     train_list.append(vv)
# random.shuffle(train_list)
# new_train.writelines(train_list)
# for a in p_test:
#     aa = a + ' 0'+'\n'
#     val_list.append(aa)
# for b in n_val:
#     bb = b + ' 1'+'\n'
#     val_list.append(bb)
# random.shuffle(val_list)
# new_val.writelines(val_list)
for c in p_test:
    cc = c + ' 0'+'\n'
    test_list.append(cc)
for d in n_test:
    dd = d + ' 1'+'\n'
    test_list.append(dd)
random.shuffle(test_list)
new_test.writelines(test_list)
# new_val.close()
# new_train.close()
new_test.close()
