import os
x=input('enter your name')
print(f'hey {x} how are you')
x=input()
print ('good')
print('1.file opening\n2.open drives\n3.open system softwares\n4.open application software\n5.exit')
x=int(input('enter your choice'))
if x==1:
    print('which files you want to open enter name it1.text file\n2.doc files\n3.program files\n')
    p=input('enter your choice')
    os.system('start c:\\')

elif x==2:
    print('2')
elif x==3:
    print('3')