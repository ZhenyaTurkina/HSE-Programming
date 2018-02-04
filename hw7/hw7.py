import re

def get_word(filename):
    # эта функция прочитывает файл и сплитит текст по возожным знакам прtпинания
    with open (filename,encoding = 'utf-8') as f:
        text = f.read()
        lines = text.splitlines()
        a = len(lines)
        b = re.split(r'[.,“"?—:;*!\n\s\t]+',text)
        a = len(b)
        return b

def suffix(word):
    # эта функция возвращает слова на 'hood'
    return word.endswith('hood')

def dict(word,freq):
    # эта функция увеличивает частотность слова каждый раз, когда оно появляется
    # в тексте
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

def word_freq(text):
    # эта функция добавляет слова в словарь и выводит их частотность
    freq = {}
    for word in text:
       if suffix(word):
           dict(word,freq)
    return freq

def derivation(text):
    # а это вообще неадекватная функция, которая выводит слова, от которых образованы
    # те слова, но в том же словаре
    freq = {}
    for word in text:
        if suffix(word):
            word = word.replace('hood', '')
            dict(word,freq)
    return freq   

def main():
    #эта функция главная
    b = get_word('slovari_P.txt')
    print ('Существительных с данным суффиксом:',word_freq(b))
    print ('Они образованы от:',derivation(b))   
    
main()

