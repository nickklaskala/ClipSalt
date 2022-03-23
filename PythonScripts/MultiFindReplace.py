import re
import sys

print('File Path:')
filePath=input().replace('"','')
# filePath=r'C:\Users\nick.klaskala\Downloads\New folder'

print('Mapping Delimiter(Type "help" for more info):')
delimiter=input()

print('Mapping:(cntl+d to complete input')
mapping=sys.stdin.read()




text=open(filePath).read()
mapping=[m.split(delimiter) for m in mapping.strip().splitlines()]


def regexReplace(old, new, str):
	return re.sub(re.escape(old), new, str, flags=re.IGNORECASE)

for pair in mapping:
	if pair[0].lower() in text.lower():
		print('found '+str(text.count(pair[0]))+' instances of text:'+pair[0])
	text=regexReplace(pair[0],pair[1],text)

file=open(filePath,'w+')
file.write(text)
file.close()

print('end')
input()
