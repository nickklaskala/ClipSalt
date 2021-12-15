import pyperclip as pc
x=pc.paste().splitlines()
xi=sorted([i.lower() for i in x])


dupes=[]
for i in range(1,len(xi)):
	if xi[i]==xi[i-1]:
		dupes.append(xi[i])
dupes=list(set(dupes))


dct={}
for i in dupes:
	dct[i]=xi.count(i)

sorted_tuples = sorted(dct.items(), key=lambda item: item[1] ,reverse=True)
sorted_dct = {k: v for k, v in sorted_tuples}

d=[]
pad=max([len(str(v)) for k,v in dct.items()])
for item,count in dct.items():
	d.append('-- '+(pad-len(str(count)))*' '+f'{count}  {item}')


print(d)


pc.copy('\n'.join(d))

