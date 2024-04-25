def rail_Encrypt(plain, num):
    cipher = ['' for i in range(num)]
    for i in range(len(plain)):
        cipher[i % num] += plain[i]
    return ''.join(cipher)


def rail_Decrypt(cipher, num):
    plain = ""
    index = 0
    while index < len(cipher):
        for i in range(num):
            if index >= len(cipher):
                break
            plain += cipher[index]
            index += 1
    return plain


def burte_force(cipher, wordlist):
    for i in range(1, len(cipher)+1):
        words = rail_Decrypt(cipher, i).split()
        count = 0
        for w in words:
            if w in wordlist:
                count += 1
        print("Number of words in wordlist: ", count,
              "out of", len(words), "words. (", i, "rails)")


def main():
    pass


if __name__ == "__main__":
    main()
