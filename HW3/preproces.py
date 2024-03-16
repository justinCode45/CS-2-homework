import string

def checkInput(input: str) -> str:
    safeInput: str = ""
    for i in input:
        if i in string.ascii_letters or i == ' ':
            safeInput += i
    return safeInput

with open("refOrigin.txt", "r") as file:
    ref = file.readlines()


for i in range(len(ref)):
    ref[i] = ref[i].lower()
    ref[i] = checkInput(ref[i])


with open("ref.txt", "w") as file:
    for i in ref:
        if i != "":
            file.writelines(i + "\n")
