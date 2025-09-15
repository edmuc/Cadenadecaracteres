
# Ejemplo 1:
palabra = input("Ingrese una palabra: ")

print("\nEjemplo 1")
print("El tipo de dato de 'palabra' es:", type(palabra))
print("La palabra", palabra, "tiene", len(palabra), "caracteres")
print("El primer carácter es:", palabra[0])
print("El último carácter es:", palabra[-1])

# Ejemplo 2: 
var = input("\nIngrese una frase: ")

print("\nEjemplo 2")
print("El tipo de dato de 'frase' es:", type(var))
print("La frase completa es:", var)
print("La frase tiene", len(var), "caracteres")
print("Los primeros 5 caracteres son:", var[0:5])


# Ejemplo 3:

print("\nDescubre la palabra oculta")
while True:
    var2 = input("Intente adivinar la palabra: ")
    
    if var2 == var:
        print("¡Usted descubrió el mensaje oculto!")
        break  # termina el bucle si acierta
    else:
        print("Palabra equivocada. Intente de nuevo.")
