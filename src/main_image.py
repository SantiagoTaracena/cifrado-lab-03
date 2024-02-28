"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo del ejercicio.
import sys
from Crypto.Cipher import AES

# Módulos necesarios para el desarrollo del ejercicio.
from encrypt_image import encrypt_image
from decrypt_image import decrypt_image

# Número de argumentos del programa.
ARGUMENTS = 4

# Verificación de los argumentos del programa.
if (len(sys.argv) != ARGUMENTS):
    print(f"Usage: {sys.argv[0]} <path> <'CBC' | 'ECB'> <key-size>")
    sys.exit(1)

# Nombre y path de la imagen.
program_name = sys.argv[0]
image_path = sys.argv[1]

# Obtención del modo a utilizar para encriptar.
if (sys.argv[2].lower() == "cbc"):
    mode = AES.MODE_CBC
elif (sys.argv[2].lower() == "ecb"):
    mode = AES.MODE_ECB
else:
    mode = str()

# Tamaño de la llave.
key_size = int(sys.argv[3])

# Encriptado y desencriptado de la imagen.
encrypted_image, key, image_size, image_name = encrypt_image(program_name, image_path, mode, key_size)
decrypt_image(program_name, encrypted_image, mode, key, image_size, image_name)
