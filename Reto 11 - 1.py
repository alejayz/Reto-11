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