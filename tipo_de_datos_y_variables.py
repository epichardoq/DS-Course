Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> X=-4
>>> X
-4
>>> X= 3.5502
>>> X
3.5502
>>> X= 2,1 + 6j
>>> X
(2, (1+6j))
>>> cadena1 = ('comillas simples')
>>> cadena1
'comillas simples'
>>> print (cadena1)
comillas simples
>>> cadena2 = ("comillas dobles")
>>> cadena2
'comillas dobles'
>>> print (cadena2)
comillas dobles
>>> n = "Aprender"
>>> n
'Aprender'
>>> a = "Python"
>>> a
'Python'
>>> n_a = n + " " + a
>>> n_a
'Aprender Python'
>>> aT = True
>>> aT
True
>>> print ("El valor es Verdadero:", aT, ", el cual es de tipo", type(aT)), "\n"
El valor es Verdadero: True , el cual es de tipo <class 'bool'>
(None, '\n')
>>> aF = False
>>> aF
False
>>> print ("El valor es Falso:", aF, ", el cual es de tipo", type(aF))
El valor es Falso: False , el cual es de tipo <class 'bool'>
>>> pla = 'pastelito', 'jamon', 'papa', 'empanadilla', 'mango', 'quesito'
>>> pla
('pastelito', 'jamon', 'papa', 'empanadilla', 'mango', 'quesito')
>>> b = ['2.36', 'elefante', 1010, 'rojo']
>>> b
['2.36', 'elefante', 1010, 'rojo']
>>> print(b)
['2.36', 'elefante', 1010, 'rojo']
>>> l4 = b[0:3:2]
>>> l4
['2.36', 1010]
>>> print(l4)
['2.36', 1010]
>>> tupla = 19645, 59621, 'hola python!'
>>> otra = tupla, (1, 5, 3, 6, 5)
>>> x, y, z = tupla
>>> print(tupla)
(19645, 59621, 'hola python!')
>>> print(otra)
((19645, 59621, 'hola python!'), (1, 5, 3, 6, 5))
>>> datos_basicos = {

"nombres":"Fran",

"apellidos":"Pardo Garcia",

"numero":"145548",

"fecha_nacimiento":"03111980",

"lugar_nacimiento":"Madrid, España",

"nacionalidad":"Portuguesa",

"estado_civil":"Casado"}
>>> print ("\nDetalle del diccionario")

Detalle del diccionario
>>> print ("=======================\n")
=======================

>>> print ("\nDetalle del diccionario")

print ("=======================\n")
SyntaxError: multiple statements found while compiling a single statement
>>> print ("\nDetalle del diccionario"), ("=======================\n")

Detalle del diccionario
(None, '=======================\n')
>>> print ("\nClaves del diccionario:", datos_basicos.keys())

Claves del diccionario: dict_keys(['nombres', 'apellidos', 'numero', 'fecha_nacimiento', 'lugar_nacimiento', 'nacionalidad', 'estado_civil'])
>>> print ("\nValores del diccionario:", datos_basicos.values())

Valores del diccionario: dict_values(['Fran', 'Pardo Garcia', '145548', '03111980', 'Madrid, España', 'Portuguesa', 'Casado'])
>>> print ("\nElementos del diccionario:", datos_basicos.items())

Elementos del diccionario: dict_items([('nombres', 'Fran'), ('apellidos', 'Pardo Garcia'), ('numero', '145548'), ('fecha_nacimiento', '03111980'), ('lugar_nacimiento', 'Madrid, España'), ('nacionalidad', 'Portuguesa'), ('estado_civil', 'Casado')])
>>> print ("\nInscripcion de Curso")

print ("====================")

print ("\nDatos de participante")

print ("---------------------")

print ("Cedula de identidad:", datos_basicos['numero'])

print ("Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos'])
SyntaxError: multiple statements found while compiling a single statement
>>> print ("\nInscripcion de Curso"),

print ("===================="),

print ("\nDatos de participante"),

print ("---------------------"),

print ("Cedula de identidad:", datos_basicos['numero']),

print ("Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos'])
SyntaxError: multiple statements found while compiling a single statement
>>> print ("\nInscripcion de Curso")

print ("====================")

print ("\nDatos de participante")

print ("---------------------")

print ("Cedula de identidad:", datos_basicos['numero'])

print ("Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos'])
SyntaxError: multiple statements found while compiling a single statement
>>> print ("\nInscripcion de Curso");
("====================")

print ("\nDatos de participante")

print ("---------------------")

print ("Cedula de identidad:", datos_basicos['numero'])

print ("Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos'])
SyntaxError: multiple statements found while compiling a single statement
>>> print ("\nInscripcion de Curso");

print ("====================");

print ("\nDatos de participante");

print ("---------------------");

print ("Cedula de identidad:", datos_basicos['numero']);

print ("Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos'])
SyntaxError: multiple statements found while compiling a single statement
>>> print ("\nInscripcion de Curso"), ("===================="), ("\nDatos de participante"), ("---------------------"), ("Cedula de identidad:", datos_basicos['numero']), ("Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos'])

Inscripcion de Curso
(None, '====================', '\nDatos de participante', '---------------------', ('Cedula de identidad:', '145548'), 'Nombre completo: Fran Pardo Garcia')
>>> print ("\nInscripcion de Curso")

Inscripcion de Curso
>>> print ("====================")
====================
>>> print ("\nDatos de participante")

Datos de participante
>>> 
======= RESTART: /Users/emmanuel/Documents/curso_python/diccionario.py =======

Detalle del diccionario
=======================


Claves del diccionario: dict_keys(['nombres', 'apellidos', 'numero', 'fecha_nacimiento', 'lugar_nacimiento', 'nacionalidad', 'estado_civil'])

Valores del diccionario: dict_values(['Fran', 'Pardo Garcia', '145548', '03111980', 'Madrid, España', 'Portuguesa', 'Casado'])

Elementos del diccionario: dict_items([('nombres', 'Fran'), ('apellidos', 'Pardo Garcia'), ('numero', '145548'), ('fecha_nacimiento', '03111980'), ('lugar_nacimiento', 'Madrid, España'), ('nacionalidad', 'Portuguesa'), ('estado_civil', 'Casado')])

Inscripcion de Curso
====================

Datos de participante
---------------------
Cedula de identidad: 145548
Nombre completo: Fran Pardo Garcia
>>> 
======= RESTART: /Users/emmanuel/Documents/curso_python/diccionario.py =======

Inscripcion de Curso
====================

Datos de participante
---------------------
Cedula de identidad: 145548
Nombre completo: Fran Pardo Garcia
>>> #Suma +
>>> g= 5+1 # g=6
>>> g
6
>>> #Resta –
>>> g= 5-1
>>> g
4
>>> #Negacion –
>>> g= -5+1
>>> g
-4
>>> #Multiplicacion *
>>> g= 5*2
>>> g
10
>>> #Exponente **
>>> g= 5**2
>>> g
25
>>> #Division /
>>> g= 5/2
>>> g
2.5
>>> #Division entera //
>>> g= 5//2
>>> g
2
>>> #Modulo: divide el operando de la izquierda por el operador del lado derecho y devuelve el resto.
>>> g= 7 % 2
>>> g
1
>>> #Division /
>>> g=7/2
>>> g
3.5
>>> r = 5 == 3
>>> r
False
>>> r = 5 != 3
>>> r
True
>>> r = 5 < 3
>>> r
False
>>> r = 5 > 3
>>> r
True
>>>  r = 5 <= 5
SyntaxError: unexpected indent
>>> r
True
>>> r = 5 <= 5
>>> r
True
>>> r = 5 >= 3
>>> r
True
>>> 
