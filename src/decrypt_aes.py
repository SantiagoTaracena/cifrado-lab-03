"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de decrypt_aes.
from Crypto.Cipher import AES

# Función decrypt_aes, para descifrar utilizando AES.
def decrypt_aes(cipher_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(cipher_text)
    return decrypted_text.rstrip(b" ")
