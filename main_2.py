

import metodos_f as mf

# Agrupamos los edificios en un diccionario para buscar sus costes por el nombre
estructuras = {
    "edificio": [500, 50, 90],
    "infraestructura": [100, 10, 33],
    "parking": [180, 30, 15],
    "chalet": [300, 30, 60],
    "parcela": [300, 100, 10],
    "farmacia": [250, 120, 20],
    "almacen": [100, 30, 40],
    "supermercado": [800, 200, 100]
}

nodos = ["edificio","infraestructura","parking","chalet","parcela","almacen","farmacia","supermercado"]
aristas = [["edificio","infraestructura"],["chalet","parcela"],["parcela","parking"],["farmacia","almacen"],["supermercado","almacen"]]

lista_edificios = [] # Lista de edificios ya construidos

#Dependencias de cada edificio, para comprobar si se puede construir o no
dependencias = {
    "edificio": "infraestructura",
    "infraestructura": "parking",
    "parking": "",
    "chalet": "parcela",
    "parcela": "parking",
    "almacen": "",
    "farmacia": "almacen",
    "supermercado": "almacen"
}


def comprobardependencia(estructura):
    # Miramos qué edificio hace falta construir antes
    requisito = dependencias[estructura]
    
    # Si no tiene requisitos (está vacío), se puede construir
    if requisito == "":
        return True
        
    # Si el requisito ya está en nuestra lista de edificios construidos
    if requisito in lista_edificios:
        return True
    else:
        print(f"Error: No está construido el requisito previo ({requisito})")
        return False


def construir(nombre_estructura):
    # 1. Comprobamos la dependencia ANTES de gastar dinero
    if not comprobardependencia(nombre_estructura):
        return # El return vacío detiene la función aquí mismo
        
    # 2. Obtenemos los datos del diccionario
    datos = estructuras[nombre_estructura]
    elemento_m = datos[0] # Materiales necesarios
    elemento_d = datos[1] # Dinero necesario
    tiempo_base = datos[2] # Tiempo base
     
    # 3. Pedimos los recursos al usuario
    print(f"--- Intentando construir: {nombre_estructura} ---")
    a = int(input(f"¿Qué materiales tienes? (Necesitas {elemento_m}): "))
    b = int(input(f"¿Qué dinero tienes? (Necesitas {elemento_d}): "))
    
    if a < elemento_m:
        print("No tienes suficientes materiales.")
        return # Detiene la función
        
    if b < elemento_d:
        print("No tienes suficiente dinero.")
        return # Detiene la función
        
    # 4. Calculamos tiempo y construimos
    obreros = int(input("¿Cuántos obreros tienes?: "))
    
    # Si hay obreros, el tiempo disminuye (tiempo_base / obreros)
    if obreros > 0:
        tiempo = mf.dividirs(tiempo_base, obreros)
    else:
        tiempo = tiempo_base
        
    # Añadimos el edificio a la lista usando paréntesis ()
    lista_edificios.append(nombre_estructura)
    print(f"¡Éxito! Construido tu {nombre_estructura} con un tiempo de {tiempo}\n")

# --- PRUEBAS ---
# Como "parking" no tiene dependencias, podemos construirlo primero:
# construir("parking")

# Una vez construido el parking, nos dejará construir la infraestructura:
# construir("infraestructura")