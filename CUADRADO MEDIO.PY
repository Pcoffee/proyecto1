
def center (size,number):
    ls = size//2
    li = size+ls
    return str(number) [-li:-ls]

def aleo_meansSquare(n, seed):
    size = len[str(seed)]
    xi = seed
    ri =[]
    for _ in range(n):
        xi = xi**2
        c = center (size, xi)
        xi = int (c)
        ri.append(float ("0." + c))
    return ri
   
if (__name__)=="__main__":
    n = int(input("ingrese el número aleatorio: "))
    seed = int(input("ingrese el valor inicial (semilla): "))
    list_random = aleo_meansSquare(n, seed)
   print(__name__)


    

