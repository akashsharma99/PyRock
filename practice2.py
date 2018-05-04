'''
Created on Jan 27, 2018
files
@author: akash
'''
f=open("readme1.txt",mode='r',encoding='utf-8')
print(f.read(200))
f.close()
f=open("readme1.txt",mode='w',encoding='utf-8')
a=['akash','mummy','papa']
f.write(input())
f.write("\nhello\nmy name is khan\n:-)\n")
lines=['hello\n','my name\n','is mogambo\n']
f.writelines(lines)
#f.write(a) // wont work, it requires only string
f.write("""the world is 
a beautiful place""")
f.close()
f=open("readme1.txt",mode='a+')
f.write("YO YO YO\n")
f.seek(0)#to shift the pointer to a specified position
print(f.read())
print(f.tell())#to show current pointer position
f.close()