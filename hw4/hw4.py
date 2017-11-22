with open("txt.txt", encoding = 'utf-8') as f:
    text = f.read() 
text = text.replace(",", "")
text = text.replace(".", "")
lol = text.split()
print(lol)

a = len(lol)

#print (a)

k = 0
s = 0

for i in range (0,a):
    if lol[i].isalpha():
        m = len(lol[i])
        if m == 3:
            k+=1
            #print (k)
        elif m == 1:
            s+=1
            #print (s)
        if m == 0:
            print ("Однобуквенных слов не существует")
        
print ("3-буквенных слов больше 1-буквенных в", k/s, "раз")
    
