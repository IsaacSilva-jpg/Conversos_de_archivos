import csv  # Libreria para leer el archivo CSV
import json # Libreria para escribir JSON 
from datetime import datetime # libreria que permite manipular fechas y horas

def convertir_tipos(fila):

    # Conversor posible edad de string a numerico entero
    if fila.get("edad"):
        try:
            fila["edad"] = int(fila["edad"])
            # aprovechando el ciclo agregamos cada fila en la lista "datos_json"
        except ValueError:
            fila["edad"] = None

    # Convertir dato "salario" de un posible string a numerico flotante 
    if fila.get("salario"):
        try:
            fila["salario"] = float(fila["salario"])
        except ValueError: 
            fila["salario"] = None

    # Cambiar fechas a formato estandar YYYY-MM-DD

    if fila.get("fecha_registro"):
        fecha = fila["fecha_registro"].strip()
        formatos = ["%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y"]  # formatos aceptados
        convertida = None

        for f in formatos:
            try:
                convertida = datetime.strptime(fecha, f).strftime("%Y-%m-%d")
                break
            except ValueError:
                pass
        
        fila["fecha_registro"] = convertida


    # Conversion de valores booleanos a True o False

    if fila.get("activo"):
        valor = fila["activo"].strip().lower()
        if valor in ("true", "1", "si", "sí", "yes"):
            fila["activo"] = True
        elif valor in ("false", "0", "no"):
            fila["activo"] = False
        else:
            fila["activo"] = None

    return fila


# una funcion con nombre csv_a_json la cual tiene dos parametros, el archivo csv y el archivo json
def csv_a_json(nombre_archivo_csv, nombre_archivo_json):

    # diccionario json en donde se guardan las filas csv convertidas a json
    datos_json = []

    # por aca abrimos y cerramos el archivo de forma segura
    # con "with" abre un archivo y lo cierre automaticamente de forma segura
    # con "open" abrimos  el archivo para leerlo o escribir sobre él, en este caso en modo lectura ("r")
    # para finalmente ponerle un alias de archivo_csv
    with open (nombre_archivo_csv, mode="r", encoding="utf-8") as archivo_csv:
        # DictReader convierte las filas en un diccionario usando los encabezados como claves
        # una vez que las filas esten en forma de diccionarios, los guadamos en la variable lector_csv 
        lector_csv = csv.DictReader(archivo_csv)
        # esta parte del codigo ejecuta un ciclo el cual "fila" recorre el diccionario antes formado 
        for fila in lector_csv:

            convertir_tipos(fila)

            datos_json.append(fila)

    # nuevamente abrimos otro archivo de forma segura en modo escritura ("w"), si no existe el archivo Python lo crea
    with open(nombre_archivo_json, mode="w", encoding="utf-8") as arhcivo_json:
        # la funcion json.dump toma la lista y la escribe dentro del archivo JSON que abrimos
        json.dump(datos_json, arhcivo_json, indent=4)

    # Mensaje para consola indica que todo el codigo se ejecuto y arroja el archivo creado
    print(f"Conversion exitosa. Archivo guardado como: {nombre_archivo_json}")

# Uso de la funcion que lee el archivo csv y lo escribe en json
csv_a_json("datos_entrada.csv", "datos_salida.json")

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# FLUJO

# El proyecto, lo primero que hace ejecuta una funcion, la cual recibe dos parametros, recibe dos archivos 
# Dentro de la funcion se hay un diccionario donde se van a guardar las filas convertidas en un diccionario
# Posteriormente leemos el archivo de entrada de forma segura, el cual es el primer parametro que maneja la funcion

# Despues abrimos otro archivo de forma segura, pero esta vez para escritura, en donde la funcion json.dump, toma la lista de 
# diccionarios (primero parametro: datos_json) y los escribe sobre el archivo representado por el segundo parametro (archivo_json) 

# Con esto se crea el archivo json el cual es un archivo fisico, no es necesario usar return para que la funcion muestre el valor 
# por que el codigo genera el archivo y queda guardado fisicamente   