"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Función pad_text para rellenar el texto plano si es necesario
def pad_text(text, pad):
    while ((len(text) % pad) != 0):
        text += b" "
    return text
