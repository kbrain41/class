# 2. Будем работать с тем же списком:
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# С помощью цикла нужно “перебрать” все языки в списке, и когда код доходит
# до “php”, цикл должен быть прерван.
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
x = 'php'
for i in languages:
    if x == i:
        print ('this languages is in list')
for i in languages:
    if x == i:
        break
