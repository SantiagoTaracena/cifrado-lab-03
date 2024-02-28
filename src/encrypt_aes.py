"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de encrypt_aes.
from Crypto.Cipher import AES

# Módulos necesarios para el desarrollo de encrypt_aes.
from pad_text import pad_text

# Función encrypt_aes, para cifrar utilizando AES.
def encrypt_aes(plain_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad_text(plain_text, 16)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text
