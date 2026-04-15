# Key expansion
# Llave original de 128 bits: 3034a1475043f4cacf4d46a8625a53f9
# AES 128 - 10 rondas (10 + llave inicial (11))

# Importar la llave
from paso0_preprocesamiento import llaveEnBytes

llaveOriginal = llaveEnBytes
def keyExpansion(llaveOriginal):
    # Se deben conseguir 11 llaves
    llaves = []
    llaves.append(llaveOriginal)
    
    # 1. Dividir en 4 subllaves, con 4 pares
    # Dividimos en pares
    pares = []
    for i in range(0, len(llaveOriginal), 2):
        par = llaveOriginal[i:i+2]
        pares.append(par)

    # Creamos 4 palabras de 4 pares
    palabras = []
    for i in range(0, len(pares), 4):
        palabra = pares[i:i+4]
        palabras.append(palabra)
    
    print("Palabras: ", palabras)

    # Necesitamos 4 palabras para cada ronda (11x4)

    # Procesar palabras
    rotWords = []

    for palabra in palabras:
        rw = rotWord(palabra)
        rotWords.append(rw)
        print("RotWord:", rw)


    # ------------------------------------------------------------
    return llaves

def rotWord(palabra):
    return palabra[1:] + palabra[:1]

keyExpansion(llaveOriginal)