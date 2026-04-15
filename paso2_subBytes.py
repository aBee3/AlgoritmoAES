from sbox import SBOX

def subBytes(bloque):
    for i in range(16):
        bloque[i] = SBOX[bloque[i]]
    return bloque
