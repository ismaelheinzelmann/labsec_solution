import base64
from string import ascii_letters

#classe base para recebimento de hexadecimais
class HexTo64:

    def __init__(self, hex: str):
        self._base64 = b''
        
        check = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        try:
            for letter in hex:
                if letter in ascii_letters: check.index(letter.upper())    
                else: check.index(letter)
        except ValueError: raise Exception("Hexadecimal Invalido")  

        self._hex = hex

    def setHex(self, hex:str):
        check = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        try:
            for letter in hex.upper():
                check.index(letter)
        except ValueError: raise Exception("Hexadecimal Invalido")  

        self._hex = hex
    
    def getHex(self):
        if self._hex == b'': raise Exception("Hexadecimal nao definido.")
        return self._hex
    
    def getHexString(self):
        str = bytes.fromhex(self.getHex())
        
        return str

    def getBase64(self):

        if self._base64 == b'':
            self._base64 = base64.b64encode(base64.b16decode(self.getHex().upper()))
            return base64.b64encode(base64.b16decode(self.getHex().upper()))
        else: return self._base64

if __name__ == "__main__":

    HEX = HexTo64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

    print(HEX.getBase64())
    print(HEX.getHex())
    print(HEX.getHexString())
