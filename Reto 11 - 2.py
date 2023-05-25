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