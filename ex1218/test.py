import random

lonum = set()

while len(lonum) < 6:
    num = random.randint(1, 45)
    lonum.add(num)

print(sorted(list(lonum)))