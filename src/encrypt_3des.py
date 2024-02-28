"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de encrypt_3des.
from Crypto.Cipher import DES

# Módulos necesarios para el desarrollo de encrypt_3des.
from pad_text import pad_text

# Función encrypt_3des, para cifrar utilizando 3DES.
def encrypt_3des(plain_text, keys):

    # Texto que se tiene durante cada etapa.
    current_text = plain_text

    # Ciclo que prueba todas las llaves existentes.
    for key in keys:
        cipher = DES.new(key, DES.MODE_ECB)
        padded_text = pad_text(plain_text, 8)
        encrypted_text = cipher.encrypt(padded_text)
        current_text = encrypted_text

    # Retorno del texto cifrado.
    return current_text
