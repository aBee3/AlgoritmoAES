#--------------------#
# Key Expansion      #
#--------------------#
# Recibe 1 llave de 16 bytes, regresa 44 "palabras" (arrays de 4 bytes)
# Equivale a 1 llave inicial, 10 subllaves para cada ronda
# Cada subllave es de 16 bytes (4 palabras c.u)

# ----------------------------------------------------------
# Llave original de 128 bits convertida a bytes
# (e.g. [48, 52, 161, 71, 80, 67, 244, 202, 207, 77, 70, 168, 98, 90, 83, 249])
from paso0_preprocesamiento import llave_bytes
from sbox import Rcon, SBOX

# ----------------------------------------------------------

def keyExpansion(llave_bytes):
    # Verificar preprocesamiento
    if len(llave_bytes) != 16:
        print(f"Error: la llave no es de 16 bytes, tiene {len(llave)}, revisar paso 0")
    
    # Inicializar array de 44 palabras
    palabras = [None] * 44
    # ----------------------------------------------------------
    # Las primeras 4 palabras son la llave original dividida en 4 partes
    # MAIN LOOP
    for i in range(4):
        palabras[i] = llave_bytes[i*4 : i*4 + 4]
    
    print("Palabras iniciales:")
    for i in range(4):
        palabras_hex = []
        for byte in palabras[i]:
            palabras_hex.append(hex(byte))
        print(f"  Palabra[{i}] = {palabras_hex}")
    print("\n")
    # ----------------------------------------------------------
    # EXPANSIÓN: crear 40 palabras restantes (para 10 subllaves)
    for i in range(4, 44):
        temp = palabras[i - 1].copy()  # Copia de la palabra anterior
        
        # Cada 4ta palabra: (1) RotWord, (2) SubWord, (3)XOR Rcon
        # La palabra "mutada" se usa para crear 4 palabras nuevas
        if i % 4 == 0:
            temp = rotWord(temp)
            temp = subWord(temp)
            temp = xorWords(temp, Rcon[i // 4]) #?

        # Nueva palabra = (temporal) XOR (palabra anterior)
        palabras[i] = xorWords(palabras[i - 4], temp)
    
    print(f"\Fin de las rondas: {len(palabras)} palabras generadas")
    return palabras

# ----------------------------------------------------------
# FUNCIONES POR RONDA
# ----------------------------------------------------------

def rotWord(word):
    # Rotar palabra un byte a la izquierda: [a,b,c,d] -> [b,c,d,a]
   rotada = word[1:] + word[:1]
   print(f"RotWord: {word} -> {rotada}")
   return rotada

def subWord(word):
    return [SBOX[b] for b in word]

def xorWords(word1, word2):
    return [word1[i] ^ word2[i] for i in range(4)]

# ----------------------------------------------------------

# Función auxiliar, crear subllave para ronda (i)
def getSubLlave(palabras, round_num):
    # Junta 4 palabras para formar una subllave
    # Forma 10 subllaves
    start = round_num * 4
    subllave = []
    for i in range(4):
        subllave.extend(palabras[start + i])
    return subllave

# Función para imprimir las subllaves
def printSubLlaves(palabras):
    # Imprime todas las subllaves (hex)
    for r in range(11):
        subllave = getSubLlave(palabras, r)
        subllave_hex = ''
        for byte in subllave:
            subllave_hex += f'{byte:02x}' # Convertirlo a hexadecimal
        print(f"Subllave ronda {r:2d}: {subllave_hex}")

# Crear y guardar subllaves
def crearSubllaves(palabras):
    subllaves = []
    for i in range(11):
        subllave = getSubLlave(palabras, i)
        subllaves.append(subllave)
    return subllaves

# ----------------------------------------------------------
# KEY EXPANSION

if __name__ == "__main__":
    llaveOriginal = llave_bytes
    print(f"Llave original: {[hex(b) for b in llaveOriginal]}\n")
    
    palabras = keyExpansion(llaveOriginal)
    
    print("\nSubllaves:\n")
    printSubLlaves(palabras)

    # Guardar subllaves
    subllaves = crearSubllaves(palabras)
    with open("subllaves.txt", "w") as archivo:
        for subllave in subllaves:
            archivo.write(f"{subllave}\n")
    print("\nSubllaves guardadas en 'subllaves.txt'\n")
# ----------------------------------------------------------