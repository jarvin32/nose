compras = []
entra = ""
while entra != "fin":
    entra = input("Ingrese un producto o 'fin' para terminar: ")
    if entra != "fin":
        compras.append(entra)

for producto in compras:
    print("compraste:", producto)