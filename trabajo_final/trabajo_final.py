from tarjetas_restaurante import *
import time

# Creamos variables.

item, sale, total, validator = {}, [], 0, True

# Realizaremos llamado a las funciones del archivo .py tarjetas.

while validator:
    print(cards(None))
    option = input("¿Qué tipo de Menú quieres? \n").lower()
    if option != "d":
        if option in ["a","b","c"]:
            p_type = {"a":"breakfast","b":"lunch","c":"dinner"}; p_type, back = p_type[option], True
            print(cards(option))
            while back:
                option = input("¿Qué plato desea?\n").lower()                  
                if option in ["h","j"] and not "a" <= option <= "g":
                    if option == "j" and option != "h": back, validator = False, False
                    else: back = False
                else:
                    plate, value = menu(option,p_type)
                    item[plate] = value; sale.append(value)
                    while 1:
                        decision = input("¿Deseas agregar algo más? (si/no)\n").lower()
                        if decision == "si": break
                        elif decision == "no": back = False; break
                        else: print("Valor inválido, inténtalo de nuevo.")
        else:
            print("Ingresó un carácter inválido.")
    else:
        break
    
# Realizamos la cuenta:

if sum(sale) > 0:
    print("Cargando lista y boleta...")
    time.sleep(2)
    print("\n|-------LISTA DE COMPRAS------|")
    for k,v in item.items():
        print(f" - {k} : S/.{v}")
    print("|-----------------------------|")
    print(f"\n{ticket(sum(sale))}")
else:
    print("Saliendo del programa...")