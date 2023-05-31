
vNiño = 0
vJoven = 0
vAdulto = 0
vAcum = 0
sw = 1
while sw == 1:   
    print("- - - BIENVENIDO AL CINE EL MORO - - -")
    print("--------------------------------------")
    print("¿CUANTAS ENTRADAS DESEAS COMPRAR?")
    print("ESTOS SON LAS CATEGORIAS Y VALORES")
    print("\n 1) - NIÑO (1-13) $5500 \n 2) - Joven (14-21) $7000 \n 3) - Adulto (<21) $9000 \n 4) - IMPRIMIR BOLETA ")

    try:
        opc = int(input(" Digite una opcion : "))
        if opc > 0 and opc < 5:
            if opc ==1:
                vCanti = int(input("Cuantas entradas vas a desear: "))
                vNiño += vCanti
                vAcum += vCanti * 5000
            elif opc ==2:
                vCanti = int(input("Cuantas entradas vas a desear: "))
                vJoven += vCanti
                vAcum += vCanti * 7000       
            elif opc ==3:
                vCanti = int(input("Cuantas entradas vas a desear : "))
                vAdulto += vCanti
                vAcum += vCanti * 9000 
            elif opc == 4:
              print("--------------- BOLETA DE PAGO ---------")
              print("por el total de ENTRADA NIÑO : ---------", vNiño,"UNIDADES")
              print("Por el total de ENTRADA JOVEN : ---------", vJoven,"UNIDADES")
              print("Por el total de ENTRADA ADULTO : -------", vAdulto,"UNIDADES")
              print("El valor de los totales a pagar es:----- $", vAcum, "")
              print(" - GRACIAS POR SU COMPRA - ")

            elif opc ==5:
              vNiño = 0
              vJoven = 0
              vAdulto = 0
              vAcum = 0
              sw = 0    
            else:
                print("Numero no valido")   
    except:
        print("Dato invalido")
print("FIN XD")        