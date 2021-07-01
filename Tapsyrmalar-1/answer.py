i = 1
while i < 20:

    for _ in range(20-i):
        print('  ', end = ' ')

    j = 1
    while j < i+1:
        if j < 10:
            print(f' {j}', end=  ' ')
        else:
            print(j, end = ' ')
        j += 1

    j = j - 1
    while j > 1:
        j -= 1
        if j < 10:
            print(f' {j}', end = ' ')
        else:
            print(j, end =  ' ')
        
    print()
    i += 1

k = 1
while k < 20:
    for _ in range(k+1):
        print('  ', end = ' ')

    j = 1
    while j < 20 - k:
        if j < 10:
            print(f' {j}', end = ' ')
        else:
            print(j, end = ' ')
        j += 1
    print()
    k += 1


