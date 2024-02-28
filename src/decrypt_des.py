"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de decrypt_des.
from Crypto.Cipher import DES

# Función decrypt_des, para descifrar utilizando DES.
def decrypt_des(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(cipher_text)
    return decrypted_text.rstrip(b" ")
