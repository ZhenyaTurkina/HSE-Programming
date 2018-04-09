import re

def get_file(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.readlines()
        return text

def main():
    x = get_file('C:\\Users\\student\\Desktop\\F.xml')
    f = open('zapis_chisla','w', encoding='utf-8')
    a = len(x)
    for i in range (a):
        if i == 75:
            break
    f.write(str(i))

if __name__ == '__main__':
    main()
