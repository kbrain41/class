names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
numbers = []
letters = []
for i in names:
    if i.isnumeric():
        nambers.append(int(i))
    else:
        letters.append(i)
print(numbers, '\n', letters)