"""
Calcula la fecha en la que cumpliras el numero de años dado.
"""
def Calculo_fecha_de_cumpleaños_segun_años_dados():   
     
    while True:
        
        nombre = input("Escribe tu nombre: ")
        
        try:
            edad  = float(input("Ingresa tu edad: "))
        except:
            print("Ingresa una edad valida.")
            continue    
        
        try:
            año = float(input("Ingresa el año en el que estas: "))
        except:
            print("Ingresa un año valido.")
            continue
        
        try:
            años_a_futuro = float(input("Ingresa el año que quieres cumplir: "))
        except:
            print("Ingresa un año valido.")
            continue
    
        fecha = int(año - edad + años_a_futuro)
        
        respuesta = f"{nombre}, vas a cumplir {años_a_futuro} años en la fecha: {fecha}"
        
        return respuesta

Calculo_fecha_de_cumpleaños_segun_años_dados()
    

   
    
    
