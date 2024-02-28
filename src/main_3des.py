"""
Universidad del Valle de Guatemala
(CC30) Cifrado de Información
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el ejercicio.
import base64

# Módulos necesarios para el ejercicio.
from generate_8byte_key import generate_8byte_key
from encrypt_3des import encrypt_3des
from decrypt_3des import decrypt_3des

# Creación del mensaje y de la clave.
message = b"Hello world"
keys = [generate_8byte_key() for _ in range(3)]

# Mensaje cifrado.
encrypted_message = encrypt_3des(message, keys)
print("Mensaje cifrado (bytes):", encrypted_message)

# Convertir los bytes a una cadena de texto utilizando Base64
encrypted_message_str = base64.b64encode(encrypted_message).decode("utf-8")
print("Mensaje cifrado (Base64):", encrypted_message_str)

# Descifrado
decrypted_message = decrypt_3des(encrypted_message, keys)
print("Mensaje descifrado:", decrypted_message.decode())
