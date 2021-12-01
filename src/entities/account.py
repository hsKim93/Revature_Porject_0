class Account:
    temp_account_id = 1

    def __init__(self, balance: int, customer_id: int):
        self.balance: int = balance
        self.customer_id: int = customer_id
        self.account_id: int = Account.temp_account_id
        Account.temp_account_id += 1

    def make_dictionary(self):
        return {
            "customerId": self.customer_id,
            "accountId": self.account_id,
            "balance": self.balance
        }