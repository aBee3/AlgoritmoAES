# Key expansion
# Llave original de 128 bits: 3034a1475043f4cacf4d46a8625a53f9
# AES 128 - 10 rondas (10 + llave inicial (11))

# Importar la llave
from paso0_preprocesamiento import llaveEnBytes

def keyExpansion(llave):

    return llave