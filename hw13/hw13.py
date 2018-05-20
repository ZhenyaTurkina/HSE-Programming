import re
import os
import operator

def main():
    empty_dict = {}
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
        for filename in files:
            i = re.search('(.+)\.(.+)', filename)
            if i.group(2) in empty_dict:
                empty_dict[i.group(2)]+=1
            else:
                empty_dict[i.group(2)] = 1
    print (empty_dict)
    print ('Файлы с расширением ' + max(empty_dict.items(), key = operator.itemgetter(1))[0] + ' встречаются чаще всего')
        
                    

if __name__ == '__main__':
    main()
