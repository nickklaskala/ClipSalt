import pyperclip as pc
x=pc.paste().splitlines()
x=x[0]
x=x.split('\t')
for i in range(0,len(x)):	
	for c in x[i]:
		if c.lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789_' and '[' not in x[i] :
			x[i]='['+x[i]+']'
print(x)
pc.copy(",".join(x))


