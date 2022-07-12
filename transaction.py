from typing import List
from hash import Hash
from operation import Operation


class Transaction:
    def __init__(self, set_of_operations: List[Operation], nonce: int):
        self.transactionID = ''
        self.setOfOperations = []
        self.nonce = 0
        self.__createTransaction(set_of_operations, nonce)

    def __createTransaction(self, set_of_operations: List[Operation], nonce: int):
        self.setOfOperations = set_of_operations
        self.nonce = nonce
        self.operations = ''
        for op in self.setOfOperations:
            self.operations += str(op)
        self.transactionID = Hash.toSHA1(self.operations + str(self.nonce))

    def printOperations(self):
        print(f'\nСписок операций транзакции:\n{self.operations}\n')

    def __str__(self):
        return f'\nID транзакции: {self.transactionID}\nNonce: {self.nonce}\n'
