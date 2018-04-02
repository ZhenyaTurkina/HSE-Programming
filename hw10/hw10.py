import re

def get_file(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.readlines()
        return text

def main():
    x = get_file('Высшая школа экономики — Википедия.html')
    all_results = re.search('Год основания(.*)title="(.*?год)"',str(x))
    if all_results:
        f = open('god_osn.txt', 'w')
        f.write(all_results.group(2))
    else:
        print ('Nothing found')


if __name__ == '__main__':
    main()
