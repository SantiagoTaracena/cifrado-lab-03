"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de encrypt_des.
from Crypto.Cipher import DES

# Módulos necesarios para el desarrollo de encrypt_des.
from pad_text import pad_text

# Función encrypt_des, para cifrar utilizando DES.
def encrypt_des(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad_text(plain_text, 8)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text
