import os
import json

file_list = os.listdir('sorted')

os_dict = {}
browser_dict = {}
device_dict = {}
model_dict = {}

for _file in file_list:
    _type = _file.split('.')[0]
    if _type == 'os':
        with open('sorted/' + _file, 'r') as f:
            for _line in f:
                split_list = _line.split('\'')
                try:
                    key_name = split_list[1] + ' ' + split_list[3]
                except IndexError:
                    key_name = split_list[1]
                _num = split_list[-1].split(',')
                _num = _num[-1].split(')')
                count = int(_num[0])
                if os_dict.get(key_name):
                    os_dict[key_name] += count
                else:
                    os_dict[key_name] = count
    elif _type == 'browser':
        with open('sorted/' + _file, 'r') as f:
            for _line in f:
                split_list = _line.split('\'')
                try:
                    key_name = split_list[1] + ' ' + split_list[3]
                except IndexError:
                    key_name = split_list[1]
                _num = split_list[-1].split(',')
                _num = _num[-1].split(')')
                count = int(_num[0])
                if browser_dict.get(key_name):
                    browser_dict[key_name] += count
                else:
                    browser_dict[key_name] = count
    elif _type == 'device':
        with open('sorted/' + _file, 'r') as f:
            for _line in f:
                split_list = _line.split('\'')
                try:
                    key_name = split_list[3]
                    model_key = split_list[5]
                except IndexError:
                    key_name = 'Other'
                    model_key = 'Other or Spider'

                _num = split_list[-1].split(',')
                _num = _num[-1].split(')')
                count = int(_num[0])

                if model_dict.get(model_key):
                    model_dict[model_key] += count
                else:
                    model_dict[model_key] = count

                if device_dict.get(key_name):
                    device_dict[key_name] += count
                else:
                    device_dict[key_name] = count

os_dict = sorted(os_dict.items(), key=(lambda x: x[1]), reverse=True)
browser_dict = sorted(browser_dict.items(), key=(lambda x: x[1]), reverse=True)
device_dict = sorted(device_dict.items(), key=(lambda x: x[1]), reverse=True)
model_dict = sorted(model_dict.items(), key=(lambda x: x[1]), reverse=True)

os_write = open('splite/os.txt', 'w')
for _line in os_dict:
    os_write.write(json.dumps(_line))
    os_write.write('\n')
os_write.close()

browser_write = open('splite/browser.txt', 'w')
for _line in browser_dict:
    browser_write.write(json.dumps(_line))
    browser_write.write('\n')
browser_write.close()

device_write = open('splite/device.txt', 'w')
for _line in device_dict:
    device_write.write(json.dumps(_line))
    device_write.write('\n')
device_write.close()

model_write = open('splite/model.txt', 'w')
for _line in model_dict:
    model_write.write(json.dumps(_line))
    model_write.write('\n')
model_write.close()
