def shiftRows(bloque):
    """
    Aplica ShiftRows a un bloque de 16 bytes
    """
    bloque = list(bloque)  # convertir a lista
    
    return [
        # Fila 0 (sin cambio)
        bloque[0], bloque[1], bloque[2], bloque[3],
        
        # Fila 1 (shift 1)
        bloque[5], bloque[6], bloque[7], bloque[4],
        
        # Fila 2 (shift 2)
        bloque[10], bloque[11], bloque[8], bloque[9],
        
        # Fila 3 (shift 3)
        bloque[15], bloque[12], bloque[13], bloque[14]
    ]
