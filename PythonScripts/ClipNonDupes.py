import pyperclip as pc
x=pc.paste().splitlines()
xi=[i.lower() for i in x]
d=[]
di=[]
for i in x:
	if i.lower() not in di and xi.count(i.lower())==1:
		d.append(i)
		di.append(i.lower())
pc.copy('\n'.join(set(d)))




