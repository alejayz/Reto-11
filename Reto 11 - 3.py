#3. progrma para obtener la matriz transpuesta

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