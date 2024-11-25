print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print(" ")#espacio
def sPos(a,b):#define funcion sPos
    for i in range(len(a)):#bucle for
        for j in range(len(b)):#bucle for
            if(a[i] == b[j]):#verifica si la condicion es verdadera
                return True #devuelve resultado si es verdadera
            else:#verifica si la condicion es falsa
                return False #devuelve resultado si es falsa
print(sPos([1,2,3,4,5],[6,7,8,9,0]))#imprime
print(sPos([1,2,3,4],[1,6,7,8,8]))#imprime
print(" ")#espacio