from account import Account
from signature import Signature


class Operation:
    def __init__(self, sender: Account, receiver: Account, amount: int, signature: int):
        self.sender = None
        self.receiver = None
        self.amount = 0
        self.signature = 0
        self.__createOperation(sender, receiver, amount, signature)

    def __createOperation(self, sender: Account, receiver: Account, amount: int, signature: int):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    @staticmethod
    def verifyOperation(operation):
        verify_signature = False
        for key_pair in operation.sender.wallet:
            if Signature.verifySignature(operation.signature, key_pair.publicKey, operation.amount):
                verify_signature = True
                break
        return operation.amount <= operation.sender.getBalance() and verify_signature

    def __str__(self):
        return f'\nОтправитель: {self.sender}\nПолучатель: {self.receiver}' \
               f'\nСумма перевода: {self.amount}\nПодпись: {self.signature}\n'
