
with open("ref.txt", "r") as file:
    ref = file.readlines()

for i in range(len(ref)):
    # Remove the newline character
    # all char will be lowercase or space   
    # change all non-alphabetic characters to space
    ref[i] = ref[i].lower()
    ref[i] = ref[i].replace("\n", "")
    ref[i] = ref[i].replace(" ", "")
    ref[i] = ref[i].replace("!", " ")
    ref[i] = ref[i].replace("@", " ")
    ref[i] = ref[i].replace("#", " ")
    ref[i] = ref[i].replace("$", " ")
    ref[i] = ref[i].replace("%", " ")
    ref[i] = ref[i].replace("^", " ")
    ref[i] = ref[i].replace("&", " ")
    ref[i] = ref[i].replace("*", " ")
    ref[i] = ref[i].replace("(", " ")
    ref[i] = ref[i].replace(")", " ")
    ref[i] = ref[i].replace("-", " ")
    ref[i] = ref[i].replace("_", " ")
    ref[i] = ref[i].replace("=", " ")
    ref[i] = ref[i].replace("+", " ")
    ref[i] = ref[i].replace("[", " ")
    ref[i] = ref[i].replace("]", " ")
    ref[i] = ref[i].replace("{", " ")
    ref[i] = ref[i].replace("}", " ")
    ref[i] = ref[i].replace(";", " ")
    ref[i] = ref[i].replace(":", " ")
    ref[i] = ref[i].replace("'", " ")
    ref[i] = ref[i].replace('"', " ")
    ref[i] = ref[i].replace("<", " ")
    ref[i] = ref[i].replace(">", " ")
    