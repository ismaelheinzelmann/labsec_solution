import Byte
from crack import score

#retorna 5 chaves melhor colocadas a partir do plain text score
def scores(SECRET: Byte.ByteObject):
    results = []

    #256 -> FF hexadecimal possibilidades
    for key in range(256):
        KEY_SECRET = Byte.ByteObject(hex(key).split('x')[1] * len(SECRET.getHex()))
        xor_iteration = SECRET^KEY_SECRET

        guess = (score(xor_iteration), key)
        if guess != None: results.append(guess)

    #naturalmente ordena pelo x[0]
    return sorted(results)

#testa as 10 chaves melhor colocadas
def crack_cipher(cipher:str):
    SECRET = Byte.ByteObject(cipher)
    
    for bit in scores(SECRET)[0:3]:
        key = bit[1]
        hex_key = str(hex(key).split('x')[1]).upper() * len(cipher)
        byteobject_key = Byte.ByteObject(hex_key)
        try:
            print(SECRET^byteobject_key)
        except Exception as e: print(e)

if __name__ == "__main__":
    cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    crack_cipher(cipher)



