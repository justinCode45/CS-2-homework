from PIL import Image 

im = Image.open("lcastle.gif")
im.show()
im.rotate(45).show()