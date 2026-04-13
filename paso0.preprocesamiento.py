#
# Preprocesamiento
#

# Importar el texto a cifrar
with open("texto.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Importar la llave
with open("llave.txt", "r", encoding="utf-8") as archivo:
    llave = archivo.read()

print(texto, llave)

# Convertir el texto a bytes
def convertirABytes(texto):
    return texto.encode('utf-8')

textoEnBytes = convertirABytes(texto)
llaveEnBytes = convertirABytes(llave)

print("Texto en bytes: ",textoEnBytes)
print("Llave en bytes: ",llaveEnBytes)

# Confirmar que es bytes
print("Formato del Texto: ", type(textoEnBytes))
print("Formato de la Llave: ", type(llaveEnBytes))

# ----------------------------------------------------------

# Dividir en bloques de 16 bytes
def dividirEnBloques(texto):
    bloques = []
    for i in range(0, len(texto), 16):
        bloque = texto[i:i+16]
        bloques.append(bloque)
    return bloques

bloques = dividirEnBloques(textoEnBytes)
print("Bloques: ",bloques)

# Confirmar que es una lista
print("Formato de los Bloques: ", type(bloques))

# ----------------------------------------------------------
