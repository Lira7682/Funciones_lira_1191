print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos
print(" ")#espacio
def isChar(s):#define funcion isChar
    if(len(s) > 1): #si longitud de 's' mayor q 1
        return False #devuelve mensaje false
    if(len(s) == 1):#si longitud de 's' igual q 1
        return True#devuelve mensaje true
def isvoc(s): #define funcion isvoc
    vocales = "aeiouáéíóú" #valor de variable vocales
    if not(s) and (isChar(s)):#verifica si la condicion es verdadera
        for i in range(len(vocales)):#bucle for
            for j in range(len(s)):#bucle for
                if (vocales[i] == s):#verifica si la condicion es verdadera
                    return True #devuelve mensaje true
                else: #verifica si la condicion es falsa
                    return False #devuelve mensaje false
    elif(s):#comprueba si una condicion es falsa
        print("El valor es un numero")#imprime mensaje si es un numero
    elif not(isChar(s)):#comprueba si una condicion es falsa
        print("El valor no es solo un caracter")#imprime mensaje 
isvoc(5)#valor de la funcion
isvoc(1)#valor de funcion
isvoc(8)#valor de funcion
print(" ")#espacio