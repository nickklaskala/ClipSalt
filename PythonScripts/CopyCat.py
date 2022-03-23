import os
import shutil

print('Copy Files From:')
fromPath=input().lower()
# fromPath='c:\\temp\\a'
if fromPath[-1]!='\\':
	fromPath=fromPath+'\\'


print('Copy Files To:')
toPath=input().lower()
# toPath='c:\\temp\\b'
if toPath[-1]!='\\':
	toPath=toPath+'\\'

print('''File Type to copy(e.g. '.txt', '.dat'):
press enter for all file types''')
FileType=input().lower()
# FileType=''#input().lower()

keepSubFolders=''
while keepSubFolders not in ('y','n'):
	print('Would you like to keep folder structure?(Y/N)')
	keepSubFolders=input().lower()
	# keepSubFolders='y'


for dirpath, dnames, fnames in os.walk(fromPath):

	for file in fnames:
		if FileType not in file.lower() and filetype!='':
			continue

		if keepSubFolders=='y':
			old=dirpath+'\\'+file
			new=toPath+dirpath.replace(fromPath,'')+'\\'
			try:
				os.makedirs(new)
			except:
				pass
			print('copying '+old+'  ------------>  '+new) 
			shutil.copy(old,new) 
		else:
			old=dirpath+'\\'+file
			new=toPath
			print('copying '+old+'  ------------>  '+new) 
			shutil.copy(old,new) 
print('please press enter to end')
input()