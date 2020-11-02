import pyperclip as pc
pc.copy(("'"+("','".join(pc.paste().splitlines()))+"'").replace("'NULL'","NULL"))



