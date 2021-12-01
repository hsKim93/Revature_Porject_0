class Account:

    def __init__(self, account_id: int, balance: float, customer_id: int):
        self.balance: float = balance
        self.customer_id: int = customer_id
        self.account_id: int = account_id

    def make_dictionary(self):
        return {
            "customerId": self.customer_id,
            "accountId": self.account_id,
            "balance": self.balance
        }