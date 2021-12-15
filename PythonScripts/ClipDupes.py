import pyperclip as pc
x=pc.paste().splitlines()
xi=sorted([i.lower() for i in x])


dupes=[]
for i in range(1,len(xi)):
	if xi[i]==xi[i-1]:
		dupes.append(xi[i])

dupes=list(set(dupes))

pc.copy('\n'.join(dupes))



