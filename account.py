from keypair import KeyPair
from signature import Signature


class Account:
    def __init__(self):
        self.accountID = None
        self.__wallet = []
        self.__balance = 0
        self.__genAccount()

    def __genAccount(self):
        kp = KeyPair(8)
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

    def signData(self, message: int, index: int):
        return Signature.signData(message, self.getWalletIndex(index))

    def __str__(self):
        return f'\nID аккаунта: {self.accountID}\nБаланс аккаунта: {self.__balance}\n'
