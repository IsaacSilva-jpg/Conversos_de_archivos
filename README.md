Automatización para Conversión de CSV a JSON

Desarrollé un script de automatizacion en Python que convierte archivos CSV en formato JSON utilizando las librerías estándar csv y json
Tecnologías: Python, csv, json.

COMO FUNCIONA:

1. Clona este repo en tu computadora, 
  git clone https://github.com/IsaacSilva-jpg/Conversos_de_archivos.git
2. Prepara un archivo CSV para colocarlo en la misma carpeta en donde esta el proyecto
3. Ejecuta el conversor
  python conversor.py datos_entrada.csv datos_salida.json
4. El script realiza la lectura del archivo CSV
   Hace una conversion automatica
   Normaliza los datos conforme al tipo de dato(numero, fecha o booleanos)
   Limpieza de valores vacios
5. Resultado: Genera un archivo Json con el nombre especificado


HABILIDADES:

  Manipulación de archivos
  Lectura y transformación de datos
  Estructuras de datos (listas, diccionarios)
  Automatización
  Mapea cada fila del CSV a un objeto JSON
  Buenas prácticas con context managers (with open)

