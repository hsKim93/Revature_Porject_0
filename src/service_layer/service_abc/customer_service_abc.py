from abc import ABC, abstractmethod
from src.entities.account import Account
from src.entities.customer import Customer


class CustomerServiceAbc(ABC):
    @abstractmethod
    def service_create_new_customer(self, first_name: str, last_name: str) -> Customer:
        pass

    @abstractmethod
    def service_get_all_customers(self) -> list[Customer]:
        pass

    @abstractmethod
    def service_get_all_accounts(self) -> list[Account]:
        pass

    @abstractmethod
    def service_get_all_customer_accounts_by_id(self, customer_id: int) -> list[Account]:
        pass

    @abstractmethod
    def service_create_new_account(self, initial_balance: int, customer_id: int) -> Account:
        pass

    @abstractmethod
    def service_get_balance_by_id(self, account_id: int) -> int:
        pass

    @abstractmethod
    def service_deposit_by_id(self, account_id: int, amount: int) -> int:
        pass

    @abstractmethod
    def service_withdraw_by_id(self, account_id: int, amount: int) -> int:
        pass

    @abstractmethod
    def service_transfer_by_ids(self, account_id_from: int, account_id_to: int, amount: int) -> list[int]:
        pass

    @abstractmethod
    def service_update_customer_information_by_id(self, first_name: str, last_name: str, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_information_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_delete_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: int) -> Customer:
        pass

