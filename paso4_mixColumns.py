# Implementacion de MixColumns de AES

# Multiplicación en GF(2^8)

def mul2(x):
    res = x << 1
    if x & 0x80:      
        res ^= 0x1b   
    return res & 0xff 


def mul3(x):
    return mul2(x) ^ x 

#Mix Columns 

def mixcolumns(nuevo): 

    bloquemix = nuevo.copy()

    # recorrer columnas (de 4 en 4)
    for i in range(0, 16, 4):
        a0 = nuevo[i]
        a1 = nuevo[i+1]
        a2 = nuevo[i+2]
        a3 = nuevo[i+3]

        # Aplicación directa de la matriz de MixColumns
        b0 = mul2(a0) ^ mul3(a1) ^ a2 ^ a3
        b1 = a0 ^ mul2(a1) ^ mul3(a2) ^ a3
        b2 = a0 ^ a1 ^ mul2(a2) ^ mul3(a3)
        b3 = mul3(a0) ^ a1 ^ a2 ^ mul2(a3)

        # Guardar resultados
        bloquemix[i]   = b0
        bloquemix[i+1] = b1
        bloquemix[i+2] = b2
        bloquemix[i+3] = b3

    return bloquemix
