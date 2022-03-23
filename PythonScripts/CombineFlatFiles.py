import os
import shutil
import pyperclip as pc

print('Combine Files in Directory:')
fromPath=input().lower()
# fromPath='C:\\Users\\nick.klaskala\\Downloads\\csvs'
if fromPath[-1]!='\\':
	fromPath=fromPath+'\\'


print('Parse String:(example "\\n GO \\n") this gets inserted between all your files')
parseStr=input().lower().replace('\\n','\n')
#parseStr=''.replace('\\n','\n')


print('''File Containing: ( myFile* , *.txt , myfile.* )''')
FileType=input().lower().replace('*','')
# FileType='.txt'.lower()

keepHeaderRecords=''
while keepHeaderRecords not in ('y','n'):
	print('Would you like to keep subsequent header records?(Y/N)')
	keepHeaderRecords=input().lower()
	#keepHeaderRecords='n'
cnt=0
returntable=[]
for dirpath, dnames, fnames in os.walk(fromPath):

	for file in fnames:
		if FileType not in file.lower() and FileType!='':
			continue

		myfile=open(dirpath+file).readlines()
		myfile[-1]=myfile[-1]+'\n' if myfile[-1][-1]!='\n' else myfile[-1]
		table=myfile
		if keepHeaderRecords=='n' and cnt!=0:
			del table[0]
		cnt+=1
		returntable.extend(table+[parseStr])
		
# print(''.join(returntable))
pc.copy(''.join(returntable))

print('combine Text Copied to clip board')



