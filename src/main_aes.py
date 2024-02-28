"""
Universidad del Valle de Guatemala
(CC30) Cifrado de Información
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el ejercicio.
import base64

# Módulos necesarios para el ejercicio.
from generate_16byte_key import generate_16byte_key
from encrypt_aes import encrypt_aes
from decrypt_aes import decrypt_aes

# Creación del mensaje y de la clave.
message = b"Hello world"
key = generate_16byte_key()

# Mensaje cifrado.
encrypted_message = encrypt_aes(message, key)
print("Mensaje cifrado (bytes):", encrypted_message)

# Convertir los bytes a una cadena de texto utilizando Base64
encrypted_message_str = base64.b64encode(encrypted_message).decode("utf-8")
print("Mensaje cifrado (Base64):", encrypted_message_str)

# Descifrado
decrypted_message = decrypt_aes(encrypted_message, key)
print("Mensaje descifrado:", decrypted_message.decode())
