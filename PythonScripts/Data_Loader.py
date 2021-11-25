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
				print('\n\n{1} UNEQUAL NUMBER OF COLUMNS ON LINE {0} PLEASE CORRECT AND RE-RUN {1}\n\n'.format(i,'*'*50))


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
		sql = ''


		sql='--drop table if exists '+dest+'\ngo\n\ncreate table '+dest+'\n(\n\trow_id int identity(1,1),\n'

		for i in range(len(headers)):
			sql+='\t'+'['+headers[i]+']'+' nvarchar('+str(self.maxColWidth[i])+'),\n'

		sql+=')\ngo\n\n'

		for i in range(0,len(table)):
			if i%1000==0:
				sql+='\ninsert into '+dest+' ('+','.join(['['+i+']' for i in headers])+')\nvalues '

			values=table[i]
			if i%1000!=0:
				sql+=','

			sql+='('+    ','.join(values)    +')\n'

		return sql







print('Delimited File Path:')
filePath=input().lower().replace('"','')
# filePath=r'C:\Users\nick.klaskala\Downloads\SANOFI_RBD_Pharmacy_Redemption_20211119012945.txt'

print('Delimiter:')
delimiter=input()
# delimiter=''

print('Quotechar:')
quotechar=input()
# quotechar=''

print('Destination Table (schema.table):')
dest=input().lower()
# dest=''


#Default Variable
if dest==None or dest=='':
	dest='#temptable'

text=open(filePath).read()
a=dataGrid(text,delimiter,quotechar)

print('Paste Query into SSMS')
print('hit enter to close')
sql=a.formatSQL()
pyperclip.copy(sql)
print('end')
input()