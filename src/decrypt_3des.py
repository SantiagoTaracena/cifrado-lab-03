"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de decrypt_3des.
from Crypto.Cipher import DES

# Función decrypt_3des, para descifrar utilizando 3DES.
def decrypt_3des(cipher_text, keys):

    # Texto que se tiene durante cada etapa.
    current_text = cipher_text

    # Ciclo que prueba todas las llaves existentes.
    for key in keys:
        cipher = DES.new(key, DES.MODE_ECB)
        decrypted_text = cipher.decrypt(cipher_text)
        current_text = decrypted_text.rstrip(b" ")

    # Retorno del texto decifrado.
    return current_text
