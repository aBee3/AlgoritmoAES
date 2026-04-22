#
# Preprocesamiento
#

# Convertir el texto a bytes, en Python se manejan como listas de enteros (0-255)

# Leer el texto (e.g. "Esto es un texto")
with open("texto.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Leer la llave (e.g. "3034a1475043f4cacf4d46a8625a53f9")
with open("llave.txt", "r", encoding="utf-8") as archivo:
    llave_hex = archivo.read().strip()

print("Texto original:", texto)
print("Llave (hex string):", llave_hex)

# Convertir el texto a bytes
texto_bytes = list(texto.encode('utf-8'))

# Convertir la llave a bytes
llave_bytes = list(bytes.fromhex(llave_hex))

print("Texto en bytes:", texto_bytes)
print("Llave en bytes:", llave_bytes)
print("Longitud de la llave:", len(llave_bytes), "bytes")

# ----------------------------------------------------------
# Creación de Bloques 
# Dividir en bloques de 16 bytes (e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
def dividirEnBloques(lista_bytes):
    bloques = []
    for i in range(0, len(lista_bytes), 16):
        bloque = lista_bytes[i:i+16]
        # Si el últoimo bloque < 16 bytes, rellenar con ceros
        if len(bloque) < 16:
            espacios_faltantes = 16 - len(bloque)
            bloque = bloque + [0] * espacios_faltantes
        bloques.append(bloque)
    return bloques
# ----------------------------------------------------------

# Dividir el texto en bloques
bloques = dividirEnBloques(texto_bytes)
print("Bloques:", bloques)
print("Número de bloques:", len(bloques))

# ----------------------------------------------------------
