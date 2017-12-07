with open ('C:\\Users\\student\\Desktop\\quotes.txt', encoding='utf-8') as f:
    text=f.read()
lines=text.splitlines()
a=len(lines)
res=[]

'''
text=text.replace('... -','')
text=text.replace('. -','')
text=text.replace('? -','')
text=text.replace('! -','')
'''

for i in range(a):
    words=lines[i].split('. — ')
    k=len(words)
    pol=words[0].split()
    if (len(pol)<=10 and len(pol[0])<5):
        print (words[0])
