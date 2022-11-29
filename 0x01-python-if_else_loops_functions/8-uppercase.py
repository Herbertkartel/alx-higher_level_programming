#!/user/bin/python3
# 8-uppercase.py
# Bayo Herbert <herbzkartel2@gmail.com>

def uppercase(str):
"""Print a string in uppercase."""
for c in string:
if ord(c) >= 97 and ord(c) <= 122:
c = chr(ord(c) - 32)
print("{}".format(c), end="")
print("")
