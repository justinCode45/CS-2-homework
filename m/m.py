
import hashlib
def decrypt(path: str):
    with open(path, 'rb') as f:
        data = f.read()
    key = hashlib.sha256("password".encode()).hexdigest()
    decrypted_data = bytearray(
        x ^ ord(key[i % len(key)]) for i, x in enumerate(data))
    return decrypted_data