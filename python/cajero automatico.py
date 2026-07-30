estudiante = {
    "nombre": "jarvin",
    "apellido": "loyo",
    "edad": 19,
    "clave": 123456,
    "saldo": 1000
}

print("bienvenido al sistema del banco nacional")
usuario = input("ingrese un usuario registrado: ")
if usuario == estudiante["nombre"]:
    print("usuario correcto")
    clave = int(input("ingrese su clave: "))
    if clave == estudiante["clave"]:
        print("clave correcta")
        print("acceso concedido")
    else:
        print("clave incorrecta")
else:
    print("usuario inexistente")


if usuario == estudiante["nombre"] and clave == estudiante["clave"]:
    menu = None
    print("bienvenido", estudiante["nombre"], estudiante["apellido"])
    while menu != 4:
        print("menu de opciones")
        print("1. consultar saldo")
        print("2. retirar dinero")
        print("3. depositar dinero")
        print("4. salir")
        menu = int(input("ingrese una opcion: "))

        if menu == 1:
            print("su saldo es de: $", estudiante["saldo"])
        elif menu == 2:
            print("retirando dinero...")
            retiro = int(input("ingrese la cantidad a retirar: "))
            if retiro <= estudiante["saldo"]:
                estudiante["saldo"] -= retiro
                print("retiro exitoso, su nuevo saldo es de: $", estudiante["saldo"])
            else:
                print("saldo insuficiente")

        elif menu == 3:
            print("depositando dinero...")
            deposito = int(input("ingrese la cantidad a depositar: "))
            estudiante["saldo"] += deposito
            print("deposito exitoso, su nuevo saldo es de: $", estudiante["saldo"])

        elif menu == 4:
            print("saliendo del sistema...")
        else:
            print("opcion invalida")