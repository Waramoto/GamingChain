from rsa import encrypt, decrypt


class Signature:
    @staticmethod
    def signData(private_key, message):
        return encrypt(private_key, message)

    @staticmethod
    def verifySignature(sign, public_key, message):
        return decrypt(public_key, sign) == message
