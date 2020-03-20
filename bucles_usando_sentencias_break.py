print('While con sentencia break')
print('===============================')

print('Sumador numero hasta 20')
sum=0
num=0
while (sum<=30):
 sum=num+sum
 num=num+1
 print('El num es ' +str(num))
 if num > 4:
   break

print('La suma es ' +str(sum) + ' y no ha llegado a 30 por el break')
