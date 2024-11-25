print (" ")#espacio
print ("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print (" ")#espacio
def suma(a):#define funcion suma
    total = 0 #valor 0 de total
    for i in range(len(a)):#bucle for
        total += a[i] #total mas o igual q a [lista]
    return total #devuelve valor de total
def mult(a): #define funcion mult
    total = 1 #total igual q 1
    for i in range(len(a)):#bucle for
        total *= a[i]#total mult o igual q a [lista]
    return total #devulve valor de total
print (suma([1,2,3,4]))#imprime resultado de funcion suma
print (mult([1,2,3,4]))#imprime resultado de funcion mult
print(" ")#espacio