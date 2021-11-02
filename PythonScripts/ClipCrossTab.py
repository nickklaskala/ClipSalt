import csv
import pandas as pd
import pyperclip as pc
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data=pc.paste().strip()

#get delimiter
dct={'|':0}
for i in set(data.splitlines()[0]):
	if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "().[]{}'):
		dct[i]=data.splitlines()[0].count(i)
delimiter=(max(dct,key=dct.get))

# data=[i.split(delimiter) for i in data.splitlines() if i !='']
data=[[l.strip() for l in row] for row in csv.reader(data.splitlines(), delimiter=delimiter, quotechar='"')]
maxLenOfFirstCol=len(max([i[0] for i in data],key=len))
df = pd.DataFrame(data[1:], columns = data[0])
ct=str(eval("pd.crosstab(df.{0},[{1}])".format(data[0][0],','.join(['df.'+c for c in data[0][1:]]))))


#pivot
ct=ct.split('\n\n')
data=[r.split('\n') for r in ct]


print(maxLenOfFirstCol)
for i in range(1,len(data)):
	data[i]=[k[maxLenOfFirstCol:] for k in data[i]]


data2=[]
for i in range(len(data[0])):
	data2.append([data[0][i]])
	for n in range(len(data)):
		if n==0:
			continue
		data2[i].append(data[n][i])
data=data2


maxList=[]
for i in range(len(data[0])):
	maxlen=0
	for r in range(len(data)):
		if len(data[r][i])>maxlen:
			maxlen=len(data[r][i])
	maxList.append(maxlen)


rst=[]
for i in range(len(data)):
	record=data[i]
	temp=[]
	for c in range(len(record)):
		temp.append(record[c]+''*(maxList[c]-len(record[c])))


	rst.append(''.join(temp))

pc.copy('\n'.join(rst))

