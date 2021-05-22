#Напишите программу, которая берёт массив данных spisok2 и выводит только те элементы из spisok_2, которых нет в spisok_1.
spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
for i in spisok_2:
    if not (i in spisok_1):
        print(i)