a = [58, 58.64, 1.02, 51, 15.25, 54.89, 5.26, 25.2, 0.2, 525.69, 5.55, 59589.4, 59, 74, 10]
print('A:')
k = 0
a_new = []
while k < len(a):
    rub = int(a[k])
    kop = int((a[k] - rub) * 100)
    price = f'{rub} руб {kop:02} коп'
    a_new.append(price)
    k += 1
print(a_new)

print('B:')
print(a, 'ID', id(a))
a.sort()
print(a, 'ID', id(a))

print('C:')
b = sorted(a, reverse=True)
print(b, 'ID', id(b))

print('D:')
c = b[:5]
print(c)
