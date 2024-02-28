"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de generate_16byte_key.
import random

# Alfabeto del cual generar llaves.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

# Función generate_16byte_key, que genera llaves de 16 bytes.
def generate_16byte_key():
    generated_key = str()
    for _ in range(16):
        generated_key += random.choice(alphabet)
    return generated_key.encode("utf-8")
