from keypair import KeyPair


class Account:
    def __init__(self):
        self.accountID = None
        self.__wallet = []
        self.__balance = 0
        self.__genAccount()

    def __genAccount(self):
        kp = KeyPair(16)
        self.addKeyPairToWallet(kp)
        self.accountID = kp.publicKey[0] + kp.publicKey[1]

    def addKeyPairToWallet(self, key_pair: KeyPair):
        self.__wallet.append(key_pair)

    def updateBalance(self, balance: int):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def getWalletIndex(self, index):
        return self.__wallet[index]

    def __str__(self):
        return f'ID аккаунта: {self.accountID}\nБаланс аккаунта: {self.__balance}'
