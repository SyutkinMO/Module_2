input_key = int(input('Введите число '))
passord = ''

for i in range(1, input_key):
    for j in range(i + 1, input_key):
        s = i + j
        if input_key % s == 0:
            passord = passord + str(i) + str(j)
        else:
            continue

print(int(passord))
