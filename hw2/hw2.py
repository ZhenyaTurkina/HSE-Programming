
word=(input('Введите слово: '))

a=len(word)

print(a)

if a==0:
    print ("Введите слово!!")
elif a==1:
    print (word, 'Слово состоит из одной буквы - слово неизменяемо')
else:
    for i in range (a - 1, -1, -1):
        if (word[i]!='з' and word[i]!='я'):
            print(word[i],end='')
