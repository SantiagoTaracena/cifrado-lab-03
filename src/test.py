from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
from io import BytesIO

image = open("./images/tux.jpg", "rb").read()
key = open("./data/ayno.key", "rb").read()

cipher = AES.new(key, AES.MODE_ECB)
encrypted_image = cipher.encrypt(pad(image, AES.block_size))

with BytesIO(encrypted_image) as byte_io:
    with Image.open(byte_io) as img:
        img.save("./out/e-output.jpeg", format="JPEG")

decrypted_image = unpad(cipher.decrypt(encrypted_image), AES.block_size)

with BytesIO(decrypted_image) as byte_io:
    with Image.open(byte_io) as img:
        img.save("./out/d-output.jpeg", format="JPEG")
