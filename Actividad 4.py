# El restaurant ZD quiere un programa con las siguientes características:
# 1. Debe tener un menú (lista) inicial con los días de la semana.
# 2. Al seleccionar una opción de la lista, debe mostrar las comidas disponibles para ese día con los costo.
# 3. Al seleccionar las comidas a consumir, el programa le indicará cuánto es el total a pagar en caja.

lunes = 10.00
martes = 11.00
miercoles = 9.50
jueves = 8.00
viernes = 12.50
total = 0.00
Salir = ""

print("                                     Restaurante ZD\n                                          ")
print("                                  Le da la bienvenidad\n                                       ")
print("                               por favor seleccione el día:\n                                  ")
print("*************************************** MENÚ SEMANAL ****************************************\n")
print(" - lunes - Setas de hamburguesa: Hamburguesa de tofu con guarnición. Precio: 10.00$\n")
print(" - marte - Buñuelos de calabacín: Tomate, queso de cabra, cebolla, pasas y orégano. Precio: 7.50$\n")
print(" - miercoles - La berenjena de la Toscana: Berenjena rellena de pimiento rojo, crema de tofu y garbanzos. Precio: 10.50$\n")
print(" - jueves - Arroz con setas y algas: Arroz integral salteado con algas hijiki. Precio: 11.00$\n")
print(" - viernes - Arroz a la paella: Arroz con mariscos mixtos. Precio: 15.00$\n")
print(" --Escriba -salir- para salir del menu.\n\n")


option=input("Escriba el dia (en minuscula) para seleccionar el menu: ")

if option == "lunes":
    total = lunes + round(lunes * 0.07,2)
    print("\nUsted a escogido LUNES: Setas de hamburguesa") 
    print("total a pagar es de:", total,"$")
elif option == "martes":
    total = martes + round(martes * 0.07,2)
    print("\nUsted a escogido MARTES: Buñuelos de calabacín")
    print("total a pagar es de:", total,"$")
elif option == "miercoles":
    total = miercoles + round(miercoles * 0.07,2)
    print("\nUsted a escogido MIERCOLES: La berenjena de la Toscana")
    print("total a pagar es de:", total,"$")
elif option == "jueves":
    total = jueves + round(jueves * 0.07,2)
    print("\nUsted a escogido JUEVES: Arroz con setas y algas")
    print("total a pagar es de:", total,"$")
elif option == "viernes":
    total = viernes + round(viernes * 0.07,2)
    print("\nUsted a escogido VIERNES: Arroz a la paella")
    print("total a pagar es de:", total,"$")
if option == "salir":
    print("\n\nRegrese pronto")

print("\nGRACIAS POR PREFERIRNOS!\n")
