import pyperclip as pc
x=pc.paste().splitlines()
x.sort()
pc.copy('\n'.join(x))