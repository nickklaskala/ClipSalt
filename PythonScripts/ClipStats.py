import pyperclip as pc
x=pc.paste().splitlines()
xi=[i.lower() for i in x]
d=[]
di=[]
for i in x:
	if i.lower() not in di:# and xi.count(i.lower())>1:
		d.append(('       '+str(xi.count(i.lower())))[-7:]+'	'+i)
		di.append(i.lower())
d.sort(reverse=True)
pad=d[0][:6].count(' ')
d=['--'+i[pad:] for i in d]
pc.copy('\n'.join(d))



