lst = [12,345,345,346,34,5,324,532,46,345,3425,36,5,43237,234,2,5,43,653,6,43,5745,723,98,763,443,53237,237]
for number in lst:
    if number % 2 == 0:
        print(number, end=' ')
    elif number == 237:
        break