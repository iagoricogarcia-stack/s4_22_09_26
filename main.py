import metodos as ms

edificio = [500, 50, 90]
infraestructura = [100, 10, 33]
parking = [180, 30, 15]
chalet = [300, 30, 60]
parcela = [300, 100, 10]
farmacia = [250, 120, 20]
almacen = [100, 30, 40]
supermercado = [800, 200, 100]

nodos= ["edificio","infraestructura","parking","chalet","parcela","almacen","parking","farmacia","supermercado"]
aristas = [["edificio","infraestructura"],["chalet","parcela"],["parcela","parking"],["farmacia","almacen"],["supermercado","almacen"]]

listadeificios = []

dependencias = {
    "edificio": ["infraestructura"],
    "infraestructura": ["parking"],
    "parking": [""],
    "chalet": ["parcela"],
    "parcela": ["parking"],
    "almacen": [""],
    "farmacia": ["almacen"],
    "supermercado": ["almacen"]
}


def construir(lista1):
     
    # Comprobamos si poseemos de los materiales y el dinero 
    a = int(input("¿Qué materiales tienes?"))
    b = int(input("¿Qué dinero tienes?"))
    
    # Preguntamos cuantos obreros usará
    obreros = int(input("¿Cuántos obreros tienes?"))
    tiempo = obreros * 0.5

    elemento_m = lista1[0]
    elemento_d = lista1[1]

    if a < elemento_m:
        print("No tienes suficientes materiales")
    if b < elemento_d:
        print("No tienes suficientes dinero")
    comprobardependencia(lista1,dependencias,listadeificios)

    listadeificios.append[]
    print(f"Construido tu {lista1} con un tiempo de {tiempo}")


def comprobardependencia(estructura, dependencias,listadeificios = []):
     if not estructura in dependencias:
          return False
     if dependencias[estructura] == [""]:
          return False
     if dependencias[estructura]in listadeificios:
          continue
     else:
          print("No esta construido")

     
