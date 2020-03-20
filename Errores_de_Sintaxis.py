def iva():

    total=int( input('cuanto has gastado'))
    num=int( input('que tipo de producto has comprado 1)leche 2)pan 3)alcohol 4)otros'))

    if num==1:

      iv=6

    elif num==2:
      iv=8

    elif num==3:
      iv=14

    else:
      iv=9

    iva1=(total*iv/100)
    print(iva1)
    return iva1


print('el iva es:')
iva()
print("Programa terminado")
