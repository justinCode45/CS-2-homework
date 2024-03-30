import zipfile

targetfile = "zilQf4LTV1L7opzfsZkXhA11iLl3VD.zip"

zfile = zipfile.ZipFile(targetfile)

print(zfile.namelist())

zfile.setpassword(b"123456")
zfile.extractall()

zfile.close()