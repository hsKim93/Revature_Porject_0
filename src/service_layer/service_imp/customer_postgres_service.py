from src.custom_exceptions.invalid_request_exception import InvalidRequestException
from src.data_access_layer.Implementation_classes.customer_postgres_dao import CustomerPostgresDao
from src.entities.account import Account
from src.entities.customer import Customer
from src.service_layer.service_abc.customer_service_abc import CustomerServiceAbc


class CustomerPostgresService(CustomerServiceAbc):
    def __init__(self, customer_dao: CustomerPostgresDao):
        self.customer_dao = customer_dao

    def service_create_new_customer(self, first_name: str, last_name: str) -> Customer:
        return self.customer_dao.create_new_customer(first_name, last_name)

    def service_get_all_customers(self) -> list[Customer]:
        return self.customer_dao.get_all_customers()

    def service_get_all_accounts(self) -> list[Account]:
        return self.customer_dao.get_all_accounts()

    def service_get_all_customer_accounts_by_id(self, customer_id: int) -> list[Account]:
        return self.customer_dao.get_all_customer_accounts_by_id(customer_id)

    def service_create_new_account(self, initial_balance: float, customer_id: int) -> Account:
        return self.customer_dao.create_new_account(initial_balance, customer_id)

    def service_get_balance_by_id(self, account_id: int) -> float:
        return self.customer_dao.get_balance_by_id(account_id)

    def service_deposit_by_id(self, account_id: int, amount: float) -> float:
        if amount <= 0:
            raise InvalidRequestException("Amount must be greater than 0")
        return self.customer_dao.deposit_by_id(account_id, amount)

    def service_withdraw_by_id(self, account_id: int, amount: float) -> float:
        balance = self.customer_dao.get_balance_by_id(account_id)
        if balance - amount < 0:
            raise InvalidRequestException("You cannot withdraw more than what you have")
        if amount < 0:
            raise InvalidRequestException("Amount must be greater than 0")
        return self.customer_dao.withdraw_by_id(account_id, amount)

    def service_transfer_by_ids(self, account_id_from: int, account_id_to: int, amount: float) -> bool:
        balance = self.customer_dao.get_balance_by_id(account_id_from)
        if balance - amount < 0:
            raise InvalidRequestException("You cannot transfer more than what you have")
        if amount < 0:
            raise InvalidRequestException("Amount must be greater than 0")
        return self.customer_dao.transfer_by_ids(account_id_from, account_id_to, amount)

    def service_update_customer_information_by_id(self, first_name: str, last_name: str, customer_id: int) -> Customer:
        return self.customer_dao.update_customer_information_by_id(first_name, last_name, customer_id)

    def service_get_customer_information_by_id(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_information_by_id(customer_id)

    def service_delete_account_by_id(self, account_id: int) -> bool:
        return self.customer_dao.delete_account_by_id(account_id)

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_by_id(customer_id)

