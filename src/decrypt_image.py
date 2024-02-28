"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para desencriptar la imagen.
import sys
import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Función decrypt_image para desencriptar una imagen.
def decrypt_image(program, encrypted_image, mode, key, original_image_size, image_name):

    # Verificación de que el modo sea correcto.
    if ((mode != AES.MODE_CBC) and (mode != AES.MODE_ECB)):
        print(f"Usage: {program} <path> <'CBC' | 'ECB'> <key-size>")
        sys.exit(1)

    # Forma original de la imagen.
    original_rows, original_cols, original_depth = original_image_size

    # Forma de la imagen encriptada.
    encrypted_rows, encrypted_cols, encrypted_depth = encrypted_image.shape
    original_rows = encrypted_rows - 1

    # Bytes de la imagen y vector de inicialización.
    encrypted_bytes = encrypted_image.tobytes()
    init_vector_size = AES.block_size if (mode == AES.MODE_CBC) else 0
    init_vector = encrypted_bytes[:init_vector_size]

    # Bytes encriptados de la imagen.
    original_image_bytes_size = original_rows * original_cols * original_depth
    padded_size = (original_image_bytes_size // AES.block_size + 1) * AES.block_size - original_image_bytes_size
    encrypted = encrypted_bytes[init_vector_size : init_vector_size + original_image_bytes_size + padded_size]

    # Instancia del decifrado y bytes de la imagen descifrada.
    cipher = AES.new(key, AES.MODE_CBC, init_vector) if (mode == AES.MODE_CBC) else AES.new(key, AES.MODE_ECB)
    decrypted_image_bytes_padded = cipher.decrypt(encrypted)
    decrypted_image_bytes = unpad(decrypted_image_bytes_padded, AES.block_size)

    # Escritura correcta de la imagen.
    lowercase_mode = "cbc" if (mode == AES.MODE_CBC) else "ecb"
    output_path = f"./out/decrypted-{image_name}-{lowercase_mode}.bmp"
    decrypted_image = np.frombuffer(decrypted_image_bytes, dtype=encrypted_image.dtype).reshape(original_rows, original_cols, original_depth)
    cv2.imwrite(output_path, decrypted_image)
    cv2.waitKey()

    # Impresión del resultado correcto
    print(f"Finished writing decrypted image {output_path}.\n")
