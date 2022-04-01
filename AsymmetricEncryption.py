from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64


class Asymmetric:

    def __init__(self):
        self.privateKey, self.publicKey = Asymmetric.generate()
        # print(self.privateKey.export_key())
        # print(self.publicKey.export_key())

    def decryptionBase64data(self, base64data):
        return Asymmetric.decryption(base64data, self.privateKey)

    def encryptionBase64data(self, data):
        return Asymmetric.encryption(data, self.publicKey)

    @staticmethod
    def generate():
        length = 1024
        privatekey = RSA.generate(length, Random.new().read)
        publickey = privatekey.publickey()
        # print(privatekey.export_key(),'\n', publickey.export_key())
        return privatekey, publickey

    @staticmethod
    def decryption(data, privatekey):
        encrypted = base64.b64decode(data)
        cipher = PKCS1_OAEP.new(privatekey)
        decrypted = cipher.decrypt(encrypted)
        return decrypted

    @staticmethod
    def encryption(data, publickey):
        cipher = PKCS1_OAEP.new(publickey)
        encrypted = cipher.encrypt(data)
        return base64.b64encode(encrypted)

    @staticmethod
    def imported_key_encryption(key, data):
        public = RSA.import_key(key)
        cipher = PKCS1_OAEP.new(public)
        encrypted = cipher.encrypt(data)
        return base64.b64encode(encrypted)


def main():
    print("Asymmetric Key")
    name = b"Mutassim ashraf"
    rsa = Asymmetric()
    encrypted = rsa.encryptionBase64data(name)
    print(encrypted)
    decrypted = rsa.decryptionBase64data(encrypted)
    print(decrypted)


if __name__ == '__main__':
    main()
