import re
import os

def main():
    file_list = os.listdir()
    i = 0
    for file in file_list:
        if os.path.isdir(file):
            if not re.search('[^А-Яа-я]',file):
                # print (file)
                i = i+1
    print ("Количество папок с кириллическими буквами: " + str(i))
    print ("Это все: " + str(file_list))

if __name__ == '__main__':
    main()
