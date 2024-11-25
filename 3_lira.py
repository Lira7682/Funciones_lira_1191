print (" ")#espacio
print ("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print (" ")#espacio
def isnum(a): #define isnum
    try: #bloque de codigo
        int(a) #numero entero, positivo o negativo
    except: #define bloque de código para ejecutar si el bloque try genera un error.
        return False; #regresa si es falso
    return True; #regresar si es verdad
def length(a): #devuelve el número de elementos
    i = 0   #variable i igual a 0
    if not (isnum(a)): #devuelve verdad si el numero es de 8 a 9
        for i in range(len(a)):#bucle for
            i = i + 1 #valor de variable i igual a i + 1
    elif(isnum(a)):#conprueba si una condicion es falsa
        return(a)#devuelve valor de variable a
    return(i)#devuelve valor de i
print(length("hola"))#imprime longitud de texto
print(length(["1","2","3"]))#imprime longitud de lista
print(" ")#espacio