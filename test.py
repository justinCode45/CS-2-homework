# import hashlib
# import io
# import PIL
# from PIL import Image
# def encrypt(path: str):
#     with open(path, 'rb') as f:
#         data = f.read()
#     key = hashlib.sha256("password".encode()).hexdigest()
#     encrypted_data = bytearray(x ^ ord(key[i % len(key)]) for i, x in enumerate(data))
#     with open(path+"C", 'wb') as f:
#         f.write(encrypted_data)
    
# def decrypt(path: str):
#     with open(path, 'rb') as f:
#         data = f.read()
#     key = hashlib.sha256("password".encode()).hexdigest()
#     decrypted_data = bytearray(x ^ ord(key[i % len(key)]) for i, x in enumerate(data))
#     with open(path+"D", 'wb') as f:
#         f.write(decrypted_data)
#     return decrypted_data

# encrypt("surprise.mygo")
# bimg = decrypt("surprise.mygoC")
# img = Image.open(io.BytesIO(bimg))
# img.show()
# img.save("form.jpg")
import compileall
compileall.compile_dir("./m")