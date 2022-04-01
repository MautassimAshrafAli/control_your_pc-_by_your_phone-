import random
from Crypto.Cipher import AES
import base64


class Symmetric:
    def __init__(self, IV, key):
        self.key = key
        self.IV = IV

    @staticmethod
    def getIV():
        return bytes(''.join([chr(random.randint(0, 0xFF)) for i in range(16)]), "utf-8")

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, data):
        obj = AES.new(self.key, AES.MODE_CBC, self.IV)
        # print(data)
        data = self.pad(data)
        ciphertext = obj.encrypt(data)
        # print(ciphertext)
        # print(base64.b64encode(ciphertext))
        return base64.b64encode(ciphertext)

    def decrypt(self, ciphertext, inBytes):

        ciphertext = base64.b64decode(ciphertext)
        aes = AES.new(self.key, AES.MODE_CBC, self.IV)
        decd = aes.decrypt(ciphertext)
        # print(str(decd).split('\\')[0].split("b'")[1])
        if inBytes:
            return decd
        else:
            return str(decd).split('\\')[0].split("b'")[1]


def main():
    print("Symmetric Key")
    key = b'0123456789abcdef'
    iv = b'0123456789abcdef'
    data = b"Decrypted Successfully"
    enc = Symmetric(iv, key)
    encrypt = enc.encrypt(data)
    print(encrypt)
    decrypt = enc.decrypt(encrypt, False)
    print(decrypt)


if __name__ == '__main__':
    main()
