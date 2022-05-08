from Byte import ByteObject

if __name__ == "__main__":
    HEX1 = ByteObject('1c0111001f010100061a024b53535009181c')
    HEX2 = ByteObject('686974207468652062756c6c277320657965')
    print(HEX2.getBytes())
    print((HEX1^HEX2).decode())