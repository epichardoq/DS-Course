print('While controlado con Evento')
print('===============================')

print('Calcular promedio')
promedio=0.1
total=0
contar=0

print('Escribe el valor (-1 para salir):')
grado=int(input())

while grado !=-1:
  total=total+grado
  contar= contar + 1
  print('Escribe el valor (-1 para salir):')
  grado=int(input())

  promedio=total/contar
  print('El promedio es ' +str(promedio))
