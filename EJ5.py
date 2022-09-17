def numeroPrimo ():
    numero: int = int(input("Introduce numero entero: "))

    if numero > 1:
        for x in range (2, numero + 1):
            if numero % x == 0 and x != numero:
                print ("El numero:", numero, "no es primo. Es divisible entre: ", x)
                break
            elif x == numero:
                print ("El numero: ", numero, "es primo")
    else:
        print("El numero debe ser mayor a 1")

numeroPrimo()