word = (input ("Введите слово: "))
list = [word]

while word != "":
    word = (input ("Введите слово: "))
    if word != "":
        list.append (word)
    if word == "":
        print ("гитлер капут")
        
a = len (list)

m = 1

with open ("kryak.txt","w",encoding='utf-8')as f:   
    for i in range (a):
        word = list [i]
        word_1 = word [m:]
        m += 1
        f.write (word_1 + '\n')




