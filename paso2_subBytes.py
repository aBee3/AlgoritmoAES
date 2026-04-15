from sbox import SBOX

def subBytes(bloque):
    return [Sbox[i] for i in bloque]
