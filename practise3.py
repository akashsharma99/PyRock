'''
Created on Jan 27, 2018
files continued
@author: akash
'''
f=open("readme2.txt",mode='w+',encoding='utf-8')
f.write('''hello world the 
game is over.''')
f.seek(0)
sentence=f.read()
f.close()
print(sentence)
words=sentence.split('o')
w=""
for x in sentence:
    w=w+x
print(w)
w=""
for x in words:
    w=w+x
print(w)

print(words)
f=open("readme2.txt",mode='rb')
print(f.tell())
f.seek(5,1)
print(f.read())
f.close()