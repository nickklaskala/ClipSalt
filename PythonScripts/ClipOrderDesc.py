import pyperclip as pc
x=pc.paste().splitlines()
x.sort(reverse=True, key=str.lower)
pc.copy('\n'.join(x))

