# -*- coding: utf-8 -*-
"""Proyecto 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/juanruiz23/12b0e12edb16a47a0ddc96cc08436f49/proyecto-3.ipynb

## Watermelon

En principio, se corroboro que el tamaño de la sandia fuera un numero entero y que cumpliera con la condicon de ser un valor entre 1 y 100 inclusive, posteriormente se realizo la operacion aritmetica para saber si el valor era par o no, si el resultado de esta operacion es exactamente cero, quiere decir que el valor es par, de ser asi, podra dividirse en dos numeros pares tambien
"""

def division_sandia(w):
  if (type(w) == int) and (w >= 1) and (w <= 100): # Se corrobora que el tamaño de la sandia fuera un numero entero entre 1 y 100
      if w%2 == 0: # Se realiza la operacion a fin de saber si el peso es par o impar
        print("Si") # Si par habra algunas forma de reescribir el peso en terminos de dos numeros pares
      else:
          print("No") # Si no es par, no podran dividir en dos numeros pares la sandia.
  else:
    print("El valor ingresado no cumple con las restricciones, debe ser un numero entero entre 1 y 100") # En caso de no cumplir las condiciones

division_sandia(50)

"""## Way Too Long Words"""

x = "hola"
y = [1,2]

len(y)
x = "hola"
type(x)

def reescritura(n,palabra):
  w = len(palabras)  # longitud de datos
  if (type(palabra) == str) and (n<=100) and (n>=10):
    s = str(w-2) # cantidad de digitos que van entre el primer y ultimo digito
    a = str(palabra[0]) # primera letra
    b = str(palabra[w-1]) # ultima letra
    print(a+s+b) # resultado
  else:
    print(palabra)

"""x[1]"""

reescritura(14,"paralelepipedo")

v = [2,1,2]



"""# Domino"""

def domino(m,n): # m: Número de filas, n: número de columnas
    if (type(m) == int) and (type(n) == int): # m y n deben ser enteros
      if (m >= 1) and (m <= n) and (n <= 16): # la condición del ejercicio para el ranfo de filas y columnas
         numero_cuadros = m*n # Cantidad de cuadros en el tablero
         numero_dominos = numero_cuadros//2 # Dividir la cantidad de cuadros en 2, para saber cuántas veces se puede colocar un domino y usar "//"" por si sobran cuadriculas cuando el tamaño del tablero es impar.
         return numero_dominos # Número de dominos
      else:
         print('Debe cumplir 1 <= m <= n <=16') # Por si no cumplen las condiciones.
    else:
       print("El número de filas y el número de columnas deben ser enteros.")# Por si no cumplen las condiciones.