from calendar import c
from Byte import ByteObject

class Encrypt:

    def __init__(self):
        pass

    def encryptByKey(self, msg : ByteObject, key : str):
        
        key_extended = ""
        counter = 0
        for _ in range(len(msg.getHex())):
            if counter == len(key): counter = 0

            key_extended += key[counter]

            
            counter += 1    

        key_byte = ByteObject(key_extended.encode('utf-8').hex())

        return msg^key_byte


