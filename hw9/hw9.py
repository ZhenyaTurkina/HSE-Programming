import re

def get_file(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
        lines = text.splitlines()
        a = len(lines)
        b = re.split(r'[«».,“"?—:;*!\n\s\t]+',text)
        a = len(b)
        return b

def main():
    x = get_file('filename')
    all_results = re.findall('[п|П]рограммир[уо]\w+[^и$][^е$]',str(x))
    if all_results:
        print (all_results)
    else:
        print('Nothing found')

if __name__ == '__main__':
    main()
