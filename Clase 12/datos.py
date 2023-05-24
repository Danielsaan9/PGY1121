#EJEMPLO DE USO  DE REPOSITORIO
print("Datos personales")
print("- - - - - - - - -")
vNom = input("Ingrese su nombre : ")
while True:

    try :

        vEdad = int(input("Ingrese su edad : "))
        break
    except:
        print("Valor no corresponde")   

print(f"Su nombre es : {vNom}")
print(f"Su edad es : {vEdad}")

