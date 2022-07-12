from block import Block
from account import Account
from transaction import Transaction
from operation import Operation


class Blockchain:
    def __init__(self, faucet_coins):
        self.coinDatabase = {}
        self.blockHistory = []
        self.txDatabase = []
        self.faucetCoins = 0
        self.__initBlockchain(faucet_coins)

    def __initBlockchain(self, faucet_coins):
        self.faucetCoins = faucet_coins
        self.blockHistory.append(Block([], ''))

    def getTokenFromFaucet(self, account: Account, amount: int):
        account.updateBalance(amount)
        self.faucetCoins -= amount

    def showCoinDatabase(self):
        print(self.coinDatabase.items())

    def validateBlock(self, block: Block):
        verify_trans_not_in_history = True
        for tr in block.setOfTransactions:
            if not verify_trans_not_in_history:
                break
            for tx in self.txDatabase:
                if tr == tx:
                    verify_trans_not_in_history = False
                    break
        verify_trans_not_conflict = True
        for tr in block.setOfTransactions:
            if not verify_trans_not_conflict:
                break
            for tx in block.setOfTransactions:
                if tr.nonce == tx.nonce and tr != tx:
                    verify_trans_not_conflict = False
                    break
        verify_operations = True
        for tr in block.setOfTransactions:
            if not verify_operations:
                break
            for o in tr.setOfOperations:
                if not Operation.verifyOperation(o):
                    verify_operations = False
                    break
        if block.prevHash == self.blockHistory[-1].blockID and verify_trans_not_in_history \
                and verify_trans_not_conflict and verify_operations:
            self.blockHistory.append(block)
            for tr in block.setOfTransactions:
                self.txDatabase.append(tr)
                for o in tr:
                    self.coinDatabase[o.sender] = o.sender.getBalance() - o.amount
                    self.coinDatabase[o.receiver] = o.receiver.getBalance() + o.amount

    def __str__(self):
        return f'\nРезерв монет: {self.faucetCoins}\nБлоки: {self.blockHistory}\n'
