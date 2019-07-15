"""
Facade: This pattern helps to provide simple unified interface to complex systems.
        It provides a single entry point to perform the required operations in the system
        by giving a high level of abstraction to the users from internal operations.

Example: Banking systems, for every transaction there will be many operations going under it like, checking balance
         deducting withdrawl amount, updating ledger (or) balance sheet, sending notifications about the transaction to user.
         All these operations are abstract to client, only operation that client will be doing is either depositing (or) withdrawing 
         amount.
""" 

"""
Main class Bank which has internal class called Account
"""
class Bank:

    """
    Account class for creating different kinds of accounts creation
    """
    class Account:
        def __init__(self,accountType):
            self.type = accountType.lower()
            self.balanceAmount = 0


    def __init__(self, accountType, moneyToDeposit):
        self.account = self.Account(accountType)
        self.account.balanceAmount = moneyToDeposit
        print("Created "+accountType+" with balance "+str(moneyToDeposit))
    
    # Checking whether sufficient amount is available to transfer
    def __checkAvailability__(self, moneyToTransfer):
        if(moneyToTransfer > self.getBalance()):
            print("Given amount to transfer is higher than available amount")
            return False
        else:
            print("Initiating transfer")
            return True

    # Displays account details
    def __printAccountDetails__(self, account):
        print("Type: "+account.type+" Balance: "+str(account.balanceAmount))

    # Provides account balance
    def getBalance(self):
        balance = self.account.balanceAmount
        return balance

    # Transfers the amount to the other accounts
    def transferAmount(self, toAccountObj, amountToTransfer):
        if(self.__checkAvailability__(amountToTransfer)):
            self.account.balanceAmount = self.account.balanceAmount - amountToTransfer
            toAccountObj.account.balanceAmount = toAccountObj.account.balanceAmount + amountToTransfer

            self.__printAccountDetails__(self.account)
            self.__printAccountDetails__(toAccountObj.account)


def main():
    savingsAccount = Bank("savings", 1000)
    investmentsAccount = Bank("investments", 500)

    savingsAccount.transferAmount(investmentsAccount, 500)

if __name__ == "__main__":
    main()