"""
Universidad del Valle de Guatemala
(CC30) Cifrado de Información
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el ejercicio.
import base64

# Módulos necesarios para el ejercicio.
from generate_8byte_key import generate_8byte_key
from encrypt_des import encrypt_des
from decrypt_des import decrypt_des

# Creación del mensaje y de la clave.
message = b"Hello world"
key = generate_8byte_key()

# Mensaje cifrado.
encrypted_message = encrypt_des(message, key)
print("Mensaje cifrado (bytes):", encrypted_message)

# Convertir los bytes a una cadena de texto utilizando Base64
encrypted_message_str = base64.b64encode(encrypted_message).decode("utf-8")
print("Mensaje cifrado (Base64):", encrypted_message_str)

# Descifrado
decrypted_message = decrypt_des(encrypted_message, key)
print("Mensaje descifrado:", decrypted_message.decode())
