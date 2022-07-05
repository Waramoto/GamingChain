from hash import Hash
from operation import Operation
from typing import List
# from account import Account
# from signature import Signature


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

    def __str__(self):
        return f'\nID транзакции: {self.transactionID}\nNonce: {self.nonce}' \
               f'\nСписок операций транзакции:\n{self.operations}\n'


# acc_sender = Account()
# acc_sender.updateBalance(10)
# kp = acc_sender.getWalletIndex(0)
#
# acc_receiver = Account()
# acc_receiver.updateBalance(3)
#
# cash = 4
# sign = Signature.signData(kp.privateKey, cash)
#
# opera = Operation(acc_sender, acc_receiver, cash, sign)
# op_list = [opera]
# trans = Transaction(op_list, 3)
# print(trans)
