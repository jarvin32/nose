def velocidad():
    while True:
        try:
            velo = float(input("Ingrese la velocidad del vehículo (km/h): "))
            if velo < 0:
                print("La velocidad no puede ser negativa. Intente nuevamente.")
            else:
                return velo
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.") 

def multa(velo):
    if velo > 110:
        print("¡Exceso de velocidad! Se aplicará una multa grave de 150.")
    elif velo >= 81:
        print("se aplicará una multa de $50 de velocidad.")
    else:
        print("Velocidad dentro del límite permitido.")

def saludo():
    print("gracias por usar el sistema de radar de velocidad. ¡Conduzca con seguridad!")

print("Bienvenido al sistema de radar de velocidad.")
entrada = velocidad()
multa(entrada)
saludo()

