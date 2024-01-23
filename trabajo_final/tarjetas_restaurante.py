from datetime import datetime
#Realizaremos una función que nos devuelva cada tarjeta que llamemos desde el otro archivo .py.
def cards(option):
    breakfast = """
|           Desayuno          |
|=============================| 
| A |Café             |S/4.50 | 
| B |Chocolate        |S/5.00 |
| C |Jugo de Fresas   |S/9.00 |
| D |Jugo de Papaya   |S/8.00 | 
| E |Pan con Pollo    |S/7.00 |
| F |Pan con Jamón    |S/7.00 |
| G |Pan con Tortilla |S/7.00 |
| H |======= REGRESAR ========|
| J |========= SALIR =========|
|=============================|"""
    lunch = """
|           Almuerzo          |
|=============================| 
| A |Tallarín verde   |S/14.50| 
| B |Puré c/pollo     |S/15.00|
| C |Escabeche c/pollo|S/19.00|
| D |Lomo saltado     |S/18.00| 
| E |Arroz Chaufa     |S/10.00|
| F |Seco de pollo    |S/12.00|
| G |Mostro           |S/11.00|
| H |======= REGRESAR ========| 
| J |======== SALIR ==========|
|=============================|"""
    dinner = """
        |    Cena    |
|=============================|
| A |Pizza Exprés     |S/9.50 |
| B |Ensalada Campera |S/7.50 |
| C |Gazpacho         |S/6.00 |
| D |Caldo de Gallina |S/6.00 |
| E |Pollo al horno   |S/5.50 |
| F |Menestrón        |S/4.00 |
| H |======= REGRESAR ========|
| G |========= SALIR =========|
|=============================|"""
    restaurant = """
|=============================|
|       RESTAURANTE OREO      |
|             MENÚ            |
|=============================|
| A |Desayuno                 |
| B |Almuerzo                 |
| C |Cena                     |
| D |========= SALIR =========|
|=============================|
¡Bienvenidos al restaurante OREO! \n"""
    if option == "a":
        return breakfast
    elif option == "b":
        return lunch
    elif option == "c":
        return dinner
    elif option == "d":
        return None
    else:
        return restaurant

def menu(section, type):
    menu = {
    "a": {"breakfast":("Café",4.50), "lunch":("Tallarín Verde",14.50), "dinner":("Pizza Exprés",9.50)},
    "b": {"breakfast":("Chocolate",5.00), "lunch":("Puré c/pollo",15.00), "dinner":("Ensalada Campera",7.50)},
    "c": {"breakfast":("Jugo de Fresa",9.00), "lunch":("Escabeche c/pollo",19.00), "dinner":("Gazpacho",6.00)},
    "d": {"breakfast":("Jugo de Papaya",8.00), "lunch":("Lomo Saltado",18.00), "dinner":("Caldo de Gallina",6.00)},
    "e": {"breakfast":("Pan con pollo",3.50), "lunch":("Arroz Chaufa",10.00), "dinner":("Pollo al Horno",5.50)},
    "f": {"breakfast":("Pan con Jamón",3.00), "lunch":("Seco de pollo",12.00), "dinner":("Menestrón",4.50)},
    "g": {"breakfast":("Pan con Tortilla",3.00), "lunch":("Mostro",11.00), "dinner":("Ají de Gallina",6.50)}
}   
    if section in [i for i in menu]:
        return menu[section][type]
    
def ticket(sale):
    ticket = f"""
    |=============================|
    |       BOLETA DE VENTAS      |
    |=============================|
      Subtotal:      S/.{sale}
      Igv:           S/.{round(sale*0.18,2)}       
      Total a pagar: S/.{round(sale*1.18,2)}       
                                
         Gracias por tu compra     
                      
                 date: {datetime.now().strftime("%d-%m-%Y")}
    |=============================|"""
    return ticket