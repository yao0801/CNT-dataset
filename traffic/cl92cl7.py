# -*- coding:utf-8 -*-
import xml.etree.cElementTree as et

root_dir = 'C:\Users\priv_data2\Desktop/'
f = open('C:\Users\priv_data2\Desktop\Priv_shanxitraffic_pre\ImageSets\clear\class_9/privshanxitraffic_class9_trainval_img2xml.txt', 'r')
path = 'C:\Users\priv_data2\Desktop\Annotations_7/'


for l in f:
    im_name = l.strip().split(' ')[0]
    xml_name = l.strip().split(' ')[1]
    xml7 = xml_name.split('/')[1]
    _xml = et.parse(root_dir + xml_name)
    root = _xml.getroot()
    for object in root.iter('object'):
        if object.find('name').text == 'pedestrian' or object.find('name').text == 'rider' or object.find('name').text == 'driver':
            object.find('name').text = 'person'

    _xml.write(path + xml7)

