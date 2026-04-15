def shiftRows(bloque):
    bloque = list(bloque)
    
    # Fila 2
    fila2 = [bloque[5], bloque[6], bloque[7], bloque[4]]
    
    # Fila 3
    fila3 = [bloque[10], bloque[11], bloque[8], bloque[9]]
    
    # Fila 4
    fila4 = [bloque[15], bloque[12], bloque[13], bloque[14]]
    
    nuevo = (
        bloque[0:4] +  # fila 1
        fila2 +
        fila3 +
        fila4
    )
    
    return nuevo
