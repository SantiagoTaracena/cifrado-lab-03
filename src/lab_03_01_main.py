"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el laboratorio.
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from PIL import Image
from io import BytesIO

# Imagen encriptada y llave a utilizar.
encrypted_image_bytes = open("./data/mr-increible_encrypted_image.jpeg", "rb").read()
hex_key = open("./data/mr-increible.key").read()
key = bytes.fromhex(hex_key)

# Proceso de desencriptado de la imagen.
cipher = AES.new(key, AES.MODE_ECB)
decrypted_image_bytes = cipher.decrypt(encrypted_image_bytes)
decrypted_image_unpad = unpad(decrypted_image_bytes, AES.block_size)

# Archivo a escribir.
decrypted_image = Image.open(BytesIO(decrypted_image_unpad))

# Imagen guardada.
decrypted_image.save("./out/result-01.jpg")
