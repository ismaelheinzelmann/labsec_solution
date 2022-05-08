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
    msg = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode('utf-8')
    key = "ICE".encode('utf-8')
    

    msg_obj = ByteObject(msg.hex())
    key_obj = ByteObject(key.hex())
    print(msg_obj^key_obj)
    