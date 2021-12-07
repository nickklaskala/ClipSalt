import csv
import pyperclip as pc
text=pc.paste().strip()

class dataGrid:

	text=''
	delimiter=''
	grid=[]
	sampleGrid=[]
	maxColWidth=[]
	sampleMaxColWidth=[]

	def __init__(self, text):
		self.text       = text.strip()
		self.delimiter  = self.getDelimiter(text)
		self.grid       = self.getGrid(self.text,self.delimiter)
		
	

	def getDelimiter(self,text):
		dct={'|':0}
		for i in set(text.splitlines()[0]):
			if i not in ('abcdefghijklmnopqrstuvwxqyzABCDEFGHIJKLMNOPQRSTUVWXQYZ0123456789_- "().[]{}'):
				dct[i]=text.splitlines()[0].count(i)
		return (max(dct,key=dct.get))

	def getGrid(self,text,delimiter):
		grid=[[l.strip() if delimiter not in l.strip() else '"'+l.strip()+'"' for l in row] for row in csv.reader(text.splitlines(), delimiter=delimiter, quotechar='"')]
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

	def getSampleGrid(self):
		self.sampleGrid=[row for row in list(self.grid)]
		for c in range(0,len(self.grid[0])):
			col=[v[c] for v in self.grid[1:]]
			col=list(set(col))
			col.sort()
			col.extend(['' for i in self.grid[1:]])
			col=col[0:len(self.grid)-1]
			for v in range(0,len(col)):
				self.sampleGrid[v+1][c]=col[v]
		self.sampleMaxColWidth=self.getMaxColumnWidth(self.sampleGrid)

	def constructTextFromGrid(self,grid,delimiter,maxColWidth=None):#list of list ie grid
		if maxColWidth==None:
			rst='\n'.join([delimiter.join(i) for i in grid])
		else:
			rst=[]
			for i in range(len(grid)):
				record , temp = grid[i] , []

				for c in range(len(record)):
					temp.append(record[c]+' '*(maxColWidth[c]-len(record[c])))
				rst.append(delimiter.join(temp))
			rst='\n'.join(rst)
		return rst

	def pivotGrid(self):
		self.grid=[list(x) for x in zip(*self.grid)]
		self.maxColWidth=self.getMaxColumnWidth(self.grid)





a=dataGrid(text)
a.pivotGrid()

temp=[]
for row in a.grid:
	if len(set(row[1:]))!=1:
		temp.append(row)
a.grid=temp
a.pivotGrid()
a.getSampleGrid()
a.pivotGrid()

rst=a.constructTextFromGrid(a.grid,'|',a.maxColWidth)
pc.copy(rst)

