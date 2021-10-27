import pyperclip as pc
x=pc.paste().splitlines()
x.sort(key=str.lower)
pc.copy('\n'.join(x))

