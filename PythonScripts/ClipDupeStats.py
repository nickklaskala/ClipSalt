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
	if i.lower() not in di:# and xi.count(i.lower())>1:
		d.append(('       '+str(xi.count(i.lower())))[-7:]+'	'+i)
		di.append(i.lower())
d.sort(reverse=True)
pad=d[0][:6].count(' ')
d=['--'+i[pad:] for i in d if '      1' not in i]
pc.copy('\n'.join(d))


