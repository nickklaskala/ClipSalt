import pyperclip as pc
x=pc.paste().splitlines()
xi=sorted([i.lower() for i in x])


dupes=[]+[x[0]]
for i in range(1,len(xi)):
	if xi[i]==xi[i-1]:
		dupes.append(xi[i])
dupes=list(set(dupes))


d=[]
di=[]
for i in dupes:
	if i.lower() not in di and xi.count(i.lower())>1:
		d.append(i)
		di.append(i.lower())
		# x.remove(i)
		xi.remove(i.lower())
pc.copy('\n'.join(set(d)))



