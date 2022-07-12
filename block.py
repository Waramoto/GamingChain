from typing import List
from transaction import Transaction
from hash import Hash


class Block:
    def __init__(self, set_of_transactions: List[Transaction], prev_hash: str):
        self.blockID = ''
        self.setOfTransactions = []
        self.prevHash = ''
        self.__createBlock(set_of_transactions, prev_hash)

    def __createBlock(self, set_of_transactions: List[Transaction], prev_hash: str):
        self.setOfTransactions = set_of_transactions
        self.prevHash = prev_hash
        self.transactions = ''
        for tr in self.setOfTransactions:
            self.transactions += str(tr)
        self.blockID = Hash.toSHA1(self.transactions + self.prevHash)

    def printTransactions(self):
        print(f'\nСписок транзакций блока:\n{self.transactions}\n')

    def __str__(self):
        return f'\nID блока: {self.blockID}\nХэш предыдущего блока: {self.prevHash}\n'
