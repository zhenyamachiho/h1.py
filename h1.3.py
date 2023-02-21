a = True
while a:
   x = input()
   if len(x) == 6:
       a = False

f3 = int(x[0]) + int(x[1]) + int(x[2])
s3 = int(x[3]) + int(x[4]) + int(x[5])

if f3 == s3:
    print('yes')
else:
    print('no')
