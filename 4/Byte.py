import Hex

#classe que herda de HexTo64 para serem feitas operações de XOR entre dois objetos ByteObject, onde toda a inserção de hexadecimais é validada
class ByteObject(Hex.HexTo64):

    def __init__(self, hex:str):
        super().__init__(hex)
        self._bytes = b''

    def getBytes(self):
        self._bytes = bytes.fromhex(self.getHex())
        return self._bytes

    #dunder para xor
    def __xor__(self, other):
        if type(other) != type(self):
            raise TypeError("Os objetos a serem iterados devem ser do tipo ByteObject")
        xor = b''

        #poderia ser iterado separadamente, mas o modulo zip facilita a interação simultânea
        for byte_self, byte_other in zip(self.getBytes(), other.getBytes()):
            xor += bytes([byte_self ^ byte_other])

        return xor

        
if __name__ == "__main__":
    HEX1 = ByteObject('1c0111001f010100061a024b53535009181c')
    HEX2 = ByteObject('686974207468652062756c6c277320657965')
    print(HEX1^HEX2)