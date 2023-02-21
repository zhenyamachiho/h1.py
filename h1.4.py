n = int(input('n = '))
m = int(input('m = '))
k = int(input('k = '))

x1 = k % n
x2 = k % m

if x1 == 0 or x2 == 0:
    print('yes')
else:
    print('no')
