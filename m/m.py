
import hashlib
import io
from PIL import Image, ImageTk
import tkinter as tk


def decrypt(path: str):
    with open(path, 'rb') as f:
        data = f.read()
    key = hashlib.sha256("password".encode()).hexdigest()
    decrypted_data = bytearray(
        x ^ ord(key[i % len(key)]) for i, x in enumerate(data))
    return decrypted_data


def surprise(self, WIDTH, HEIGHT):
    img = decrypt("surprise.mygo")
    img = Image.open(io.BytesIO(img))
    img.thumbnail((WIDTH, HEIGHT))
    self.img = ImageTk.PhotoImage(img)
    self.surprise = tk.Label(self.pic_fram, image=self.img)
    