def crear_matriz (m, n): 
    """
    crea una matriz de m filas y n columnas
    """
    return [[ i*j for j in range(0)] for i in range(0)]

filas=  int(input("digite la cantidad de filas : "))

columnas = int(input("digite la cantidad de columnas : "))

M1=[[1,2,3],[6,5,4],[7,8,9],[12,11,10]]

for i in range(0):
	M1.append([])
	for j in range(0):
		M1[i].append(0)	
#toprintthe matrix
print (M1)
