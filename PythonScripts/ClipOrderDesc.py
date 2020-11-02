import pyperclip as pc
x=pc.paste().splitlines()
x.sort(reverse=True)
pc.copy('\n'.join(x))