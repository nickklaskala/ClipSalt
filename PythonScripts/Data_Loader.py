from pathlib import Path
import os
import pyperclip
import csv


class dataGrid:

	text=''
	delimiter=''
	quotechar=''
	grid=[]
	sampleGrid=[]
	maxColWidth=[]
	sampleMaxColWidth=[]

	def __init__(self, text,delimiter,quotechar):
		self.text       = text.strip()
		self.delimiter  = delimiter if delimiter !=None and delimiter!='' else self.getDelimiter(self.text)
		self.quotechar  = quotechar if quotechar !=None and quotechar!='' else '"'
		self.grid       = self.getGrid()
		
		for i in range(len(self.grid)):
			if len(self.grid[i])!=len(self.grid[0]):
				print('\n\n{1} UNEQUAL NUMBER OF COLUMNS ON LINE {0} IN FILE  PLEASE CORRECT AND RE-RUN {1}\n'.format(i,'*'*50))


	def getDelimiter(self,text):
		dct={'|':0}#default hardcode cause i said so
		for i in set(text.splitlines()[0]):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "().[]{}'):
				dct[i]=text.splitlines()[0].count(i)
		return (max(dct,key=dct.get))

	def getGrid(self):
		grid=[[l.strip() if self.delimiter not in l.strip() else '"'+l.strip()+'"' for l in row] for row in csv.reader(text.splitlines(), delimiter=self.delimiter, quotechar=self.quotechar)]
		self.maxColWidth= self.getMaxColumnWidth(grid)
		return grid


	def getMaxColumnWidth(self,grid):
		maxColWidth=[]
		for i in range(len(grid[0])):
			maxlen=0
			for r in range(len(grid)):
				try:
					if len(grid[r][i])>maxlen:
						maxlen=len(grid[r][i])
				except:
					pass
			maxColWidth.append(maxlen)
		return maxColWidth


	def formatSQL(self):

		headers=self.grid[0]
		table=[["'"+f.replace("'","''")+"'" if f!='' else 'NULL' for f in row] for row in a.grid[1:] ]
		table=[',('+','.join(row)+')\n' for row in table]

		sql='--drop table if exists '+dest+'\ngo\n\ncreate table '+dest+'\n(\n\trow_id int identity(1,1),\n'

		for i in range(len(headers)):
			sql+='\t'+'['+headers[i]+']'+' nvarchar('+str(self.maxColWidth[i])+'),\n'
		sql+='\n)\n'
		insert='\n\ngo\n\ninsert into '+dest+' ('+','.join(['['+i+']' for i in headers])+')\nvaluesxfillerx'

		if len(table)>1000:
			tableInsertLocs=[1000*i-1 for i in range(1,int(len(table)/1000)+1)]
			while tableInsertLocs:
				loc=tableInsertLocs.pop()
				table.insert(loc,insert)
		table.insert(0,insert)

		sql+=''.join(table)
		sql=sql.replace('valuesxfillerx,','values ').replace('valuesxfillerx','values')

		return sql




print('Delimited File Path:')
filePath=input().lower().replace('"','')
#filePath=r'C:\Users\nick.klaskala\Downloads\'

print('Delimiter:')
delimiter=input()
# delimiter=''

print('Quotechar:')
quotechar=input()
# quotechar=''

print('Destination Table (schema.table):')
dest=input().lower()
# dest=''

sql=''
sql2='\n'
#Default Variable


if dest==None or dest=='':
	dest=os.path.basename(filePath)
	dest='#'+dest.split('.')[0]

if Path(filePath).is_file():
	text=open(filePath).read()
	a=dataGrid(text,delimiter,quotechar)
	sql+=a.formatSQL()
	sql2+='\nselect * from '+dest
else:
	for path, folders, files in os.walk(filePath):
		for file in files:
			dest='#'+os.path.basename(path+'\\'+file).split('.')[0]
			text=open(path+'\\'+file).read()
			print('Reading '+file+'...\n')
			a=dataGrid(text,delimiter,quotechar)
			sql+=a.formatSQL()
			sql2+='\nselect * from '+dest




print('Paste Query into SSMS')
print('hit enter to close')
pyperclip.copy(sql+sql2)
# print(sql+sql2)
print('end')
input()

