# Reto-11
# Hello! :wave:

Para este nuevo reto tenemos como objetivo darle solución a los siguientes puntos:

**1.** Desarrollar un programa que permita realizar la suma/resta de matrices.

```python
#Desarrollar un programa para suma y resta de matrices.

def Matriz(Fil,Colum):  #se definene las variables de la funcion
  m1 = [] # se crea una lista vacía para elmacenar los elementos de la matriz
  for i in range(Fil):
    filas =[] #lista vacía para almacenar los elementos de la filas con el ciclo for
    for j in range(Colum):
        n = int(input(f"Ingrese un número [{i}][{j}]: ")) #para que los elementos ingresados se ubiquen en la matriz
        filas.append(n) #se agregan los elementos de las filas
    m1.append(filas) #todo queda dentro de la matriz
  return m1

def SumaMatrices(A, B):
  Suma = [] #lista vacía para almacenar los elementos de la suma de matrices
  for i in range(len(A)): #toma cada uno de los elementos de las filas de las matrices
    M = []
    for j in range(len(A[0])): #toma cada uno de los elementos de las columnas de las matrices
      M.append(A[i][j] + B[i][j]) #realiza la suma de los elementos en ambas matrices
        
    Suma.append(M) #los resultados de la suma se agregan a la matriz resultante
  return Suma

def RestaMatrices(A, B):
  Resta = [] #lista vacía para almacenar los elementos de la resta de matrices
  for i in range(len(A)): #toma cada uno de los elementos de las filas de las matrices
    M = []
    for j in range(len(A[0])): #toma cada uno de los elementos de las columnas de las matrices
      M.append(A[i][j] - B[i][j]) #realiza la resta de los elementos en ambas matrices

    Resta.append(M) #los resultados de la resta se agregan a la matriz resultante
  return Resta
      
  

if __name__ == "__main__":  
  Fil = int(input("Ingrese num de filas: ")) #se ingresa la cantidad de filas de la matriz
  Colum = int(input("Ingrese num de columnas: ")) #se ingresa la cantidad de columnas de la matriz
  MatrizA = Matriz(Fil,Colum) #se evalúa la función para formar las matriz 1
  print("A:", MatrizA)
  MatrizB = Matriz(Fil,Colum) #se evalúa la función para formar las matriz 2
  print("B:", MatrizB)
  if len(MatrizA) == len(MatrizB) and len(MatrizA[0]) == len(MatrizB[0]): # se verifica que ambas matrices tengan el mismo número de filas y columnas
    Suma = SumaMatrices(MatrizA, MatrizB) #se evalúa la función para restar las matrices
    Resta = RestaMatrices(MatrizA, MatrizB) #se evalúa la función para restar las matrices
    print("Sí se pueden realizar la suma y la resta de matrices")
    print("La suma de las matrices es: " + str(Suma))
    print("la resta de las matrices es: " + str(Resta))
  else:
    print("No se puede realizar la suma ni la resta de matrices")
```

**2.** Desarrollar un programa que permita realizar el producto de matrices.

```python
#2. Programa para calcular el producto de matrices

def Matriz(Fil,Colum):  #se definenen las variables de la funcion
  m = [] # se crea una lista vacía para elmacenar los elementos de la matriz
  for i in range(Fil):
    filas =[] #lista vacía para almacenar los elementos de la filas con el ciclo for
    for j in range(Colum):
        n = int(input(f"Ingrese un número [{i}][{j}]: ")) #para que los elementos ingresados se ubiquen en la matriz
        filas.append(n) #se agregan los elementos de las filas
    m.append(filas) #todo queda dentro de la matriz
  return m


def ProductoMatrices(A, B): #se definen los productos de la funcion
  Producto = [] #lista vacía para almacenar los elementos de la matriz del producto
  for i in range(len(A)):
      Producto.append([])
      for j in range(len(B[0])):
        Producto[i].append(0)

  for i in range(len(A)): #toma cada uno de los elementos de las filas de las matrices
    for j in range(len(B[0])):#toma cada uno de los elementos de las columnas de las matrices
      for k in range(len(A[0])): #toma cada uno de los elementos de las columnas de las matrices
       Producto[i][j] += A[i][k] * B[k][j] #realiza la multiplicación de los elementos de las columnas de una matriz por las filas de la otra.
  return Producto

if __name__ == "__main__":  
  Fil = int(input("Ingrese num de filas: ")) #se ingresa la cantidad de filas de la matriz
  Colum = int(input("Ingrese num de columnas: ")) #se ingresa la cantidad de columnas de la matriz
  MatrizA = Matriz(Fil,Colum) #se evalúa la función para formar las matriz 1
  print("A:", MatrizA)
  MatrizB = Matriz(Fil,Colum) #se evalúa la función para formar las matriz 2
  print("B:", MatrizB)
  if len(MatrizA[0]) == len(MatrizB): # se verifica que las colu,mnas de la matriz A sean iguales al  número de filas dede la matriz B
    Product = ProductoMatrices(MatrizA, MatrizB) #se evalúa la función para multiplicar las matrices
    print("Sí se pueden realizar la suma y la resta de matrices")
    print("El producto de las matrices es: " + str(Product))
  else:
    print("No se puede realizar la multiplicación de las matrices")
```

**3.** Desarrollar un programa que permita obtener la matriz transpuesta de una matriz ingresada.

```python
#3. programa para obtener la matriz transpuesta

def Matriz(Fila,Columna):  #se definenen las variables de la funcion
  m = [] # se crea una lista vacía para elmacenar los elementos de la matriz
  for i in range(Fila):
    filas =[] #lista vacía para almacenar los elementos de la filas con el ciclo for
    for j in range(Columna):
        n = int(input(f"Ingrese un número [{i}][{j}]: ")) #para que los elementos ingresados se ubiquen en la matriz
        filas.append(n) #se agregan los elementos de las filas
    m.append(filas) #todo queda dentro de la matriz
  return m

def MatrizTranspuesta(A):
  Transp = [] #lista vacía para almacenar los elementos de la suma de matriz transpuesta
  for i in range(len(A[0])): #toma cada uno de los elementos de las filas de la matriz
    Transp.append([])
    for j in range(len(A)): #toma cada uno de los elementos de las columnas de la matricez
      Transp[i].append(A[j][i]) #realiza el cambio de pocisión entre los elementos de las filas y columnas de la matriz

  return Transp


if __name__ == "__main__":  
  Fila = int(input("Ingrese numero de filas: ")) #se ingresa la cantidad de filas de la matriz
  Columna = int(input("Ingrese numero de columnas: ")) #se ingresa la cantidad de columnas de la matriz
  Matriz = Matriz(Fila,Columna) #se evalúa la función
  print("M:", Matriz)
  Mtranspuesta = MatrizTranspuesta(Matriz) #se evalúa la función para hacer la trnaspocisión de la matriz
  print("la matriz transpuesta es: " + str(Mtranspuesta))
```

**4.** Desarrollar un programa que sume los elementos de una columna dada de una matriz.

**5.** Desarrollar un programa que sume los elementos de una fila dada de una matriz.
