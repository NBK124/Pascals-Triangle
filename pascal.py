pas = [[1], [1, 1]]
n = int(input('Введите номер ряда: '))
if n >= 2:
    for _ in range(n - 1):
        temp = [1]
        for i in range(1, len(pas[-1])):
            temp.append(pas[-1][i - 1] + pas[-1][i])
        temp.append(1)
        pas.append(temp)
print(*pas[n])
