# Key expansion
# Llave original de 128 bits: 3034a1475043f4cacf4d46a8625a53f9
# AES 128 - 10 rondas (10 + llave inicial (11))

# Importar la llave
from paso0_preprocesamiento import llaveEnBytes
from sbox import Rcon
from sbox import SBOX

llaveOriginal = llaveEnBytes

# KEY EXPANSION
def keyExpansion(llaveOriginal):
    # Se deben conseguir 11 llaves, 44 palabras
    llaves = [None] * 44  # 44 palabras
    llaves[0] = llaveOriginal

    # 0. Dividir en 4 subllaves, con 4 pares
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
    
    # Palabras de la llave original
    print("Palabras: ", palabras)

    # Llave original + 4 nuevas palabras
    for i in range(4):
        llaves[i] = palabras[i]
    
    # Llaves iniciales
    print("Llaves: ", llaves)

    # Main loop: expandir llave
    for i in range(4, 44):
        llave_temp = llave[i - 1]

        if i % 4 == 0:
            # 1. Rotar palabra
            llave_temp = rotWord(llave_temp) 
            # 2. Substituir bytes
            llave_temp = sBox(llave_temp) 
            # 3. XOR con Rcon
            llave_temp = xor(llave_temp, Rcon[i//4])

        #llaves[i] = xor(llaves[i - 4], llave_temp)       # XOR with previous 4th word
    

    # ------------------------------------------------------------
    return llaves

def rotWord(palabra):
    return palabra[1:] + palabra[:1]

def sBox(palabra):
    for i in range(4):
        palabra[i] = SBOX[palabra[i]]
    return palabra

def xor(palabra, rcon):
    return

keyExpansion(llaveOriginal)