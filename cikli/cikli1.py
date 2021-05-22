# 1. Допустим у нас есть список языков программирования.
#   lang1 = 'Rust'
#   languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#   если переменная в списке, то нужно вывеvсти на экран 'this languages is in list'
#   Если этого языка нет в
#   списке, ничего не нужно выводить.

languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
x = 'rust'
for i in languages:
    if x == i:
        print ('this languages is in list')
