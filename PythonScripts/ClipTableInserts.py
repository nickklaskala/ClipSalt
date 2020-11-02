import os
import pyperclip as pc

delimiter='	'
dest='#temptable'
file=pc.paste().splitlines()

table=[f for f in file[1:]]
headers=file.pop(0).replace('\n','').split(delimiter)
sql=''

for f in range(0,len(table)):
	values=table[f]
	values=[j if j!='' else 'NULL' for j in values.replace('\n','').split(delimiter)]
	values=[j.replace("'","''") for j in values]
	values=["'"+j+"'" if j !='NULL' else 'NULL' for j in values]
	table[f]=values
	sql+='('
	sql+=','.join(values)
	sql+=')\n'



sql='--Drop Table if exists '+dest+'\ngo\n\ncreate table '+dest+'\n(\n\trow_id int identity(1,1),\n'
for i in range(0,len(headers)):
	maxlen=0
	for r in range(0,len(table)):
		if len(table[r][i])>maxlen:
			maxlen=len(table[r][i])
	sql+='\t'+'['+headers[i]+']'+' nvarchar('+str(maxlen)+'),\n'

sql+=')\ngo\n\n'


for i in range(0,len(table)):

	if i%1000==0:
		sql+='\ninsert into '+dest+' ('

		for x in range(0,len(headers)):
			if x!=0:
				sql+=', '
			sql=sql+'['+headers[x]+']'

		sql+=')\nvalues '


	values=table[i]
	if i%1000!=0:
		sql+=','
	
	sql+='('
	sql+=','.join(values)
	sql+=')\n'



pc.copy(sql)



