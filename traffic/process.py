# -*- coding:utf-8 -*-
import xml.etree.cElementTree as et

root_dir = 'C:\Users\priv_data2\Desktop\Annotations_9/'
f = open('', 'r')
f_sb = open('', 'w')
f_uc = open('', 'w')

l_uc = []

for l in f:
    im_name = l.strip().split(' ')[0]
    xml_name = l.strip().split(' ')[1]

    _xml = et.parse(root_dir + xml_name)
    root = _xml.getroot()
    same = []
    # i = 0
    for object in root.iter('object'):
        pose = object.find('pose')
        truncated = object.find('truncated')
        difficult = object.find('difficult')
        if pose == None or truncated == None or difficult == None:
            if l not in l_uc:
                l_uc.append(l)
            else:
                pass

        category = object.find('name')
        bbox = object.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        xmax = int(bbox.find('xmax').text)
        ymin = int(bbox.find('ymin').text)
        ymax = int(bbox.find('ymax').text)
        boundingbox = (ymin, ymax, xmin, xmax)
        same.append(boundingbox)
        # i += 1
    # print i
    if len(same) != len(set(same)):
        f_sb.writelines(l)

    _xml.write(root_dir + xml_name)

f_sb.close()

for i in l_uc:
    f_uc.writelines(i)
f_uc.close()