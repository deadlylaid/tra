import os
import json

dir_list = os.listdir('pack')

os_dict = {}
device_dict = {}
browser_dict = {}

key_list = []
value_list = []
for _file in dir_list:
    _type = _file.split('_')[0]
    type_file = _file.split('_')[0] + '.txt'

    with open('pack/'+_file, 'r') as f:
        for i, v in enumerate(f):
            if i % 2 == 0:
                key_list.append(v)
            else:
                value_list.append(v)

    for index in range(len(key_list)):
        if _type == 'os':
            os_dict[key_list[index]] = int(value_list[index])
        elif _type == 'device':
            device_dict[key_list[index]] = int(value_list[index])
        elif _type == 'browser':
            browser_dict[key_list[index]] = int(value_list[index])
    key_list = []
    value_list = []

os_dict = sorted(os_dict.items(), key=(lambda x: x[1]), reverse=True)
device_dict = sorted(device_dict.items(), key=(lambda x: x[1]), reverse=True)
browser_dict = sorted(browser_dict.items(), key=(lambda x: x[1]), reverse=True)

os_sorted = open('sorted/os.txt', 'w')
device_sorted = open('sorted/device.txt', 'w')
browser_sorted = open('sorted/browser.txt', 'w')

for i in os_dict:
    os_sorted.write(str(i))
    os_sorted.write('\n')
os_sorted.close()

for j in device_dict:
    device_sorted.write(str(j))
    device_sorted.write('\n')
device_sorted.close()

for z in browser_dict:
    browser_sorted.write(str(z))
    browser_sorted.write('\n')
browser_sorted.close()
