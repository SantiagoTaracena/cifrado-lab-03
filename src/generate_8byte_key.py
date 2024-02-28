"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo de generate_8byte_key.
import random

# Alfabeto del cual generar llaves.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

# Función generate_8byte_key, que genera llaves de 8 bytes.
def generate_8byte_key():
    generated_key = str()
    for _ in range(8):
        generated_key += random.choice(alphabet)
    return generated_key.encode("utf-8")
