print (" ")#espacio
print ("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print (" ")#espacio
def mayor3(a,b,c): #define funcion mayor3
    if((a > b) and (a > c)):  #verifica si 'a' mayor 'b' y 'a' mayor 'c'
        return a   #regresa valor de a
    if((b > a) and (b > c)): #verifica si 'b' mayor 'a' y 'b' mayor 'c'
        return b  #regresa valor de b
    if((c > a) and (c > b)):#verifica si 'c' mayor 'a' y 'c' mayor 'b'
        return c   #regresa valor de c
print(mayor3(16,12,3)) #imprime valor mayor 
print (" ")#espacio