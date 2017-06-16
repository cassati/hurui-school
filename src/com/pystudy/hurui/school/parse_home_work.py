'''
Created on 2017年6月16日

@author: zkw
'''

import re

def readFile(file_name):
    with open(file_name, encoding='utf-8') as f:
        origin_data = f.read()
    
    pattern_input = re.compile(r'<input.*?\s/>')
    inputs = re.findall(pattern_input, origin_data)
    
    pattern_id = re.compile(r'<input\sid="(.*)"\stype.*')
    ids = []
    for tmp in inputs:
        if tmp.find('checked="checked"') >= 0:
            match = pattern_id.match(tmp)
            if match:
                ids.append(match.group(1))

    msg = '--yes'
    for id in ids:
        label = r'<label\sfor="'+id+'">' + '(.*?)' + '</label>'
        pattern_label = re.compile(label)
        label_finded = re.findall(pattern_label, origin_data)
        if label_finded[0].find(msg) < 0:
            label_replace = '<label for="'+id+'">' + label_finded[0] + msg + '</label>'
            origin_data = re.sub(pattern_label, label_replace, origin_data)
    
    # 删除个人信息
    pattern_user = r'<span\sid="ContentPlaceHolder1_lbCourse".*?</span>'
    origin_data = re.sub(pattern_user, '', origin_data)
    
    # 删除logo
    pattern_header = r'<div\sid="logo".*?</div>'
    origin_data = re.sub(pattern_header, '', origin_data)
    
    # 删除欢迎信息
    pattern_welcome = r'<div\sid="liveclock".*?</div>'
    origin_data = re.sub(pattern_welcome, '', origin_data)
    
    # 删除查看作业
    pattern_homework = r'<div><span\sid="lbNavigate".*?</span></div>'
    origin_data = re.sub(pattern_homework, '', origin_data)
    
    f = open(file_name, 'w', encoding='utf-8')
    f.write(origin_data)
    f.flush()
    f.close()
    print(file_name + ' 处理完成')
    
if __name__ == '__main__':
    readFile(r'd:\《护理学基础B》第1次作业.html')
    
    
    