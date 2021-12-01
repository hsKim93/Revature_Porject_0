from src.entities.account import Account


class Customer:

    def __init__(self, customer_id, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.customer_id: int = customer_id
        self.account_list: list[Account] = []

    def make_dictionary(self):
        account_dict = []

        for account in self.account_list:
            account_dict.append(account.make_dictionary())

        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "customerId": self.customer_id,
            "accounts": account_dict
        }
