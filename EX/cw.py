import re
import os
import csv

def creat_csv (filename):
    f = open (filename, 'w', encoding = 'utf-8')
    table = f.write("doc_id;title;author;created;topic;tagging")
    f.close()
    return table

def get_data(file_name):
    ''' прочесть содержимое файла '''
    with open(file_name, encoding='utf-8') as f:
        raw_text = f.read()
    return raw_text


def pos_freq(text):
    '''  '''
    pos = re.findall(r'gr="([A-Z-]+)\W', text)
    pos_freq_d = {p: pos.count(p) for p in pos}
    return pos_freq_d
    

if __name__ == '__main__':
    filename_csv = creat_csv('users.txt')
    file_list = os.listdir("news")
    list = []
    for file in file_list:
        with open('news\\' + file, encoding='utf-8') as f:
                raw_text = f.read()
                docid = re.search(r'content=(.*)name="docid"',str(raw_text))
                list.append (docid.group(1))
                with open('users.txt','w') as f:
                    f.write (str(list) + '\n')
    spisok = []
    for file in file_list:
        with open('news\\' + file, encoding='utf-8') as f:
                raw_text = f.read()
                title = re.search(r'<title>(.*)</title>',str(raw_text))
                spisok.append (title.group(1))   
                with open('users.txt','a') as f:
                    f.write (str(spisok) + '\n')

    spisok_1 = []
    for file in file_list:
        with open('news\\' + file, encoding='utf-8') as f:
                raw_text = f.read()
                author = re.search(r'content=(.*)name="author"',str(raw_text))
                spisok_1.append (author.group(1))   
                with open('users.txt','a') as f:
                    f.write (str(spisok_1) + '\n')

    spisok_2 = []
    for file in file_list:
        with open('news\\' + file, encoding='utf-8') as f:
                raw_text = f.read()
                created = re.search(r'content=(.*)name="created"',str(raw_text))
                spisok_2.append (created.group(1))   
                with open('users.txt','a') as f:
                    f.write (str(spisok_2) + '\n')
            
    spisok_3 = []
    for file in file_list:
        with open('news\\' + file, encoding='utf-8') as f:
                raw_text = f.read()
                topic = re.search(r'content=(.*)name="topic"',str(raw_text))
                spisok_3.append (topic.group(1))   
                with open('users.txt','a') as f:
                    f.write (str(spisok_3) + '\n')

    spisok_4 = []
    for file in file_list:
        with open('news\\' + file, encoding='utf-8') as f:
                raw_text = f.read()
                tagging = re.search(r'content=(.*)name="tagging"',str(raw_text))
                spisok_4.append (tagging.group(1))   
                with open('users.txt','a') as f:
                    f.write (str(spisok_4) + '\n')
