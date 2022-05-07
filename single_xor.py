import fixed_xor
from crack import score

#retorna 5 chaves melhor colocadas a partir do plain text score
def scores(SECRET: fixed_xor.ByteObject):
    results = []

    #256 bits
    for key in range(256):
        KEY_SECRET = fixed_xor.ByteObject(hex(key).split('x')[1] * len(SECRET.getHex()))
        xor_iteration = SECRET.iterate(KEY_SECRET)

        guess = (score(xor_iteration), key)
        if guess != None: results.append(guess)

    #naturalmente ordena pelo x[0]
    return sorted(results)

#testa as 5 chaves (em bits) melhor colocadas
def crack_cipher(cipher:str):
    SECRET = fixed_xor.ByteObject(cipher)
    
    for bit in scores(SECRET)[0:5]:
        key = bit[1]
        hex_key = str(hex(key).split('x')[1]).upper() * len(cipher)
        byteobject_key = fixed_xor.ByteObject(hex_key)
        try:
            print(SECRET.iterate(byteobject_key))
        except Exception as e: print(e)

if __name__ == "__main__":
    cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    crack_cipher(cipher)



