input_key = int(input('Введите число '))
work_key = []
out_key = []
a = 1
chet_ = 1
nechet_ = 0

while a <= input_key:
    work_key.append(a)
    a = a+1
t = len(work_key)//2
# print(t)
print (work_key)

for i in range (work_key[0], work_key[t]):
    for k in range (work_key[1], work_key[-1]):
        s = i + k
        if input_key % s == 0 and i != k:
            new_ = True
            while nechet_ <= len(out_key):
                if len(out_key) == 0:
                    break
                elif i == out_key[chet_] and k == out_key [nechet_]:
                    new_ = False
                    break
                else:
                    chet_ +=2
                    nechet_ +=2
                    continue
            if new_:
                out_key.append(i)
                out_key.append(k)
            else:
                continue

print (*out_key)