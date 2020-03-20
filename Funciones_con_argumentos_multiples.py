def calcula_media(*args):
  total = 0
  for i in args:
    total += i
    resultado = total / len(args)
  return resultado

a, b, c, d, e = 3, 5, 10, 15, 160
media = calcula_media(a, b, c, d, e)
print("La media es:")
print(media)
print("Programa terminado")
