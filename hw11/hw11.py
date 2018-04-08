import re

def get_file(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.readlines()
        return text

def main():
    f = open('changed.txt','w', encoding='utf-8')
    x = get_file('Лингвистика — Википедия.html')
    all_results = re.sub('([^А-Яа-я])Язык(а|у|е|ом|и|ов|ам|ами|ах)?([^А-Яа-я])','\\1Шашлык\\2\\3',str(x))
    all_results = re.sub('([^А-Яа-я])язык(а|у|е|ом|и|ов|ам|ами|ах)?([^А-Яа-я])','\\1шашлык\\2\\3',str(all_results))
    if all_results:
        f.write(all_results + '\n')
    else:
        print ('Nothing found')


if __name__ == '__main__':
    main()
