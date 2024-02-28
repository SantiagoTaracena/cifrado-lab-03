"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Ejercicio - Pycryptodome, DES y AES
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para encriptar la imagen.
import sys
import cv2
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Función encrypt_image para encriptar una imagen.
def encrypt_image(program, image_path, mode, key_size):

    # Verificación de que el modo sea correcto.
    if ((mode != AES.MODE_CBC) and (mode != AES.MODE_ECB)):
        print(f"Usage: {program} <path> <'CBC' | 'ECB'> <key-size>")
        sys.exit(1)

    # Lectura de la imagen y su forma.
    original_image = cv2.imread(image_path)
    original_rows, original_cols, original_depth = original_image.shape

    # Ancho mínimo que debe tener la imagen.
    min_width = (AES.block_size + AES.block_size) // original_depth + 1

    # Verificación de que el ancho de la imagen sea el mínimo.
    if (original_cols < min_width):
        print(f"Minimum width must be {min_width} pixels.")
        sys.exit(1)

    # Imagen original pasada a bytes.
    original_image_bytes = original_image.tobytes()

    # Llave y vector de inicialización.
    key = get_random_bytes(key_size)
    init_vector_size = AES.block_size if (mode == AES.MODE_CBC) else 0
    init_vector = get_random_bytes(init_vector_size)

    # Cifrado del texto perteneciente a la imagen.
    cipher = AES.new(key, AES.MODE_CBC, init_vector) if (mode == AES.MODE_CBC) else AES.new(key, AES.MODE_ECB)
    original_image_padded_bytes = pad(original_image_bytes, AES.block_size)
    cipher_text = cipher.encrypt(original_image_padded_bytes)

    # Conversión de los bytes encriptados a imagen.
    padded_size = len(original_image_padded_bytes) - len(original_image_bytes)
    void = original_cols * original_depth - init_vector_size - padded_size
    init_vector_cipher_text_void = init_vector + cipher_text + bytes(void)
    encrypted_image = np.frombuffer(init_vector_cipher_text_void, dtype=original_image.dtype).reshape(original_rows + 1, original_cols, original_depth)

    # Escritura correcta de la imagen.
    lowercase_mode = "cbc" if (mode == AES.MODE_CBC) else "ecb"
    image_name = image_path.split("/")[-1].split(".")[0]
    output_path = f"./out/{image_name}-{lowercase_mode}.bmp"
    cv2.imwrite(output_path, encrypted_image)
    cv2.waitKey()

    # Impresión del resultado correcto.
    print(f"\nFinished writing image {output_path}.")

    # Retorno de la llave para su uso al desencriptar.
    return encrypted_image, key, (original_rows, original_cols, original_depth), image_name
