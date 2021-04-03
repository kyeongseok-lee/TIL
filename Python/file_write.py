import random

hg = list('가나라다라마바사아자차카타파하')

with open('file.txt', 'w') as info:
    for i in range(10):
        name = random.choice(hg) + random.choice(hg)
        weight = random.randrange(40, 100)
        height = random.randrange(150, 200)
        info.write(f'{name}, {weight}, {height}\n')

        