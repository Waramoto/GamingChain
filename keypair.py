from rsa import keys_gen


class KeyPair:
    def __init__(self, key_size):
        self.privateKey = None
        self.publicKey = None
        self.__genKeyPair(key_size)

    def __genKeyPair(self, key_size):
        kp = keys_gen(key_size)
        self.publicKey = kp[0]
        self.privateKey = kp[1]

    def __str__(self):
        return f'Приватный ключ: {self.privateKey}\nПубличный ключ: {self.publicKey}'
