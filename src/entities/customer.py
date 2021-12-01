from src.entities.account import Account


class Customer:

    def __init__(self, customer_id: int, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.customer_id: int = customer_id

    def make_dictionary(self):
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "customerId": self.customer_id
        }
