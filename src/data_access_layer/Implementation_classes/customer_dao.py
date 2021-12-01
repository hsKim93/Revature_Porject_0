from src.data_access_layer.abstract_classes.customer_dao_abc import CustomerDaoAbc
from src.entities.account import Account
from src.entities.customer import Customer


class CustomerDao(CustomerDaoAbc):
    # database
    customer_list = []
    account_list = []

    customer_one = Customer("Hyungsuk", "Kim")
    account_one = Account(5000, customer_one.customer_id)
    customer_one.account_list.append(account_one)

    customer_two = Customer("Jonathan", "Kim")
    account_two = Account(1000, customer_two.customer_id)
    customer_two.account_list.append(account_two)

    customer_list.append(customer_one)
    customer_list.append(customer_two)

    account_list.append(account_one)
    account_list.append(account_two)

    def create_account(self, initial_balance: int, customer_id: int) -> Account:
        for customer in CustomerDao.customer_list:
            if customer.customer_id == customer_id:
                account = Account(initial_balance, customer.customer_id)
                customer.account_list.append(account)
                CustomerDao.account_list.append(account)
                return account

    def get_balance_by_id(self, account_id: int) -> int:
        for account in CustomerDao.account_list:
            if account.account_id == account_id:
                return account.balance

    def deposit_by_id(self, account_id: int, amount: int) -> int:
        for account in CustomerDao.account_list:
            if account.account_id == account_id:
                account.balance += amount
                return account.balance

    def withdraw_by_id(self, account_id: int, amount: int) -> int:
        for account in CustomerDao.account_list:
            if account.account_id == account_id:
                account.balance -= amount
                return account.balance

    def transfer_by_ids(self, account_id_from: int, account_id_to: int, amount: int) -> bool:
        for account_one in CustomerDao.account_list:
            if account_one.account_id == account_id_from:
                for account_two in CustomerDao.account_list:
                    if account_two.account_id == account_id_to:
                        account_one.balance -= amount
                        account_two.balance += amount
                        return True
            if account_one.account_id == account_id_to:
                for account_two in CustomerDao.account_list:
                    if account_two.account_id == account_id_from:
                        account_one.balance += amount
                        account_two.balance -= amount
                        return True
        return False

    def update_customer_information_by_id(self, first_name: str, last_name: str, customer_id: int) -> Customer:
        for customer in CustomerDao.customer_list:
            if customer.customer_id == customer_id:
                customer.first_name = first_name
                customer.last_name = last_name
                return customer

    def get_customer_information_by_id(self, customer_id: int) -> Customer:
        for customer in CustomerDao.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def delete_account_by_id(self, account_id: int) -> Account:
        for account in CustomerDao.account_list:
            if account.account_id == account_id:
                CustomerDao.account_list.remove(account)
                return account

    def delete_customer_by_id(self, customer_id: int) -> Customer:
        for customer in CustomerDao.customer_list:
            if customer.customer_id == customer_id:
                CustomerDao.customer_list.remove(customer)
                return customer

    def create_new_customer(self, first_name: str, last_name: str) -> Customer:
        pass

    def get_all_customers(self) -> list[Customer]:
        pass

    def get_all_accounts(self) -> list[Account]:
        pass

    def get_all_customer_accounts_by_id(self, customer_id: int) -> list[Account]:
        pass
