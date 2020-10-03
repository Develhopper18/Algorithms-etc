import random

def search(listes,n):
    i = 0
    
    while i< len(listes):
        if listes[i] == n:
            globals()["pos"] = i
            return True
        i = i + 1

    return False

listes =[5,8,6,9,2] # Array or a list
# listes.append(p)
print(listes)
n = 9

if search(listes,n):
    print("found at", pos)
else:
    print("not found")