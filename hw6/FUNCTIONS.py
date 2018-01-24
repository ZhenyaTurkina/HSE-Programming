import random

def get_word(filename):
    # эта функция прочитывает файл и выбирает рандомное слово из списка
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()
        words = text.split(',')
        w = random.choice(words)
        return w

def adj_capital():
    # эта функция берет слово из прилагательныых, начинающихся с заглавной буквы
    w = get_word("adject_capital_letters.txt")
    return w

def adj_non_capital():
    # эта функция берет слово из прилагательных, начинающихся на строчную букву
    w = get_word("adject _non-capital.txt")
    return w

def noun():
    # эта функция берет одно существительное
    w = get_word("nouns.txt")
    return w

def adverbs():
    # эта функция берет одно наречие
    w = get_word("adverbs.txt")
    return w

def verbs():
    # эта функция берет один глагол
    w = get_word("verbs.txt")
    return w

def additions():
    # эта функция берет... дополнение или что-то вроде того
    w = get_word("additions.txt")
    return w

def imperative():
    # эта функция берет повелительный глагол
    w = get_word("imperative.txt")
    return w



def aff():
    # эта функция генерирует утвердительное предложение с рандомным знаком препинания
    punct = random.choice(['.','!','...'])
    sent = adj_capital() + " " + noun() + " " + adverbs() + " " + verbs() + " " + additions() + punct 
    return sent

def question():
    # эта функция генерирует вопросительное предложение с рандомным знаком препинания
    punct = random.choice(['?','?..','?!'])
    sent = adj_capital() + " " + noun() + " " + adverbs() + " " + verbs() + " " + additions() + punct 
    return sent

def negative():
    # эта функция генерирует отрицательное предложение с рандомным знаком препинания
    punct = random.choice(['.','...','!'])
    sent = adj_capital() + " " + noun() + " " + adverbs() + " " + "не" + " " + verbs() + " " + additions() + punct
    return sent

def condition():
    # эта функция генерирует условное предложение с рандомным знаком препинания
    punct = random.choice(['.','!','...'])
    sent = "Если" + " "  + adj_non_capital() + " " + noun() + " " + adverbs() + " " + verbs() + " " + additions() + "," + " " + "то" + " " + adj_non_capital() + " " + noun() + " " + adverbs() + " " + verbs() + " " + additions() + punct
    return sent

def imperative_s():
    # эта функция генерирует утвердительное предложение с рандомным знаком препинания
    punct = random.choice(['!','.','...'])
    sent = adj_capital() + ' ' + noun() + ',' + ' ' + imperative() + ' ' + additions() + punct
    return sent


def order():
    # эта функция генерирует случайный порядок предложений
    text = ''
    list_of_sent = [aff(),question(),negative(),condition(),imperative_s()]
    random.shuffle(list_of_sent)
    for i in range(len(list_of_sent)):
        text += list_of_sent[i]
        if i != len(list_of_sent) - 1:
            text += '\n'
    return text

def main():
    # основная функция, которая выводит текст
    print(order())
    
main()
