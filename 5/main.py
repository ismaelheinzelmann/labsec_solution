from Byte import ByteObject
from Encrypt import Encrypt

if __name__ == '__main__':
    msg_hex = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode('utf-8').hex()
    MSG = ByteObject(msg_hex)
    KEY = "ICE"

    encrypt = Encrypt()

    print(encrypt.encryptByKey(MSG,KEY).hex())