import random

def get_word(filename):
    with open (filename, encoding = 'utf-8') as f:
        text = f.readlines()
        return text

def creat(raw_text):
    creation = {}
    for line in raw_text:
        splitted = line.split(',')
        adj = splitted[0]
        adj = adj.strip()
        noun = splitted[1]
        noun = noun.strip()
        if adj in creation:
            creation[adj] = creation[adj] + noun
        else:
            creation[adj] = noun         
    return creation
    
def main():
    q = 0
    N = 1
    raw_data = get_word('spisok_slovosochetanii.csv')
    creation = creat(raw_data)
    values = []
    keys = []
    indexes = []
    for noun in creation.values():
         values.append(noun)
    n = random.choice(values)
    for i, j in enumerate(values):
        if j == n:
            indexes.append(i)
    random_index = random.choice(indexes)
    for adj in creation.keys():
        keys.append(adj)
    print ("Здрасьте, вы попали в шоу Кривой Код. Я загадал слово, гы. Вот вам подсказочка. Подсказка: " + keys[random_index] + " ...")
    while q == 0:
        dlina = len(keys[random_index])
        enter = (input ("Введите же слово: "))
        if enter == n:
            print ("Вы великолепны!")
            break
        else:
            if N == dlina:
                print ("Лавочка закрыта... приходите в следующий раз!")
                break
            else:
                print ("Подумайте еще!")
                N = N + 1

if __name__ == '__main__':
    main()
