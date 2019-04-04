#f(x):x*10
#f(x,y):x**y


p=lambda x,y:x**y
print(p(10,2))
names=['alex_','Mathew__','_Simon_']
cleaned_name=list(map(lambda x: x.replace('_'," "),names))
print(cleaned_name)