from abc import abstractmethod, ABC
from src.entities.account import Account
from src.entities.customer import Customer


class CustomerDaoAbc(ABC):

    @abstractmethod
    def create_account(self, initial_balance: float, customer_id: int) -> Account:
        pass

    @abstractmethod
    def get_balance_by_id(self, account_id: int) -> float:
        pass

    @abstractmethod
    def deposit_by_id(self, account_id: int, amount: float) -> float:
        pass

    @abstractmethod
    def withdraw_by_id(self, account_id: int, amount: float) -> float:
        pass

    @abstractmethod
    def transfer_by_ids(self, account_id_from: int, account_id_to: int, amount: float) -> bool:
        pass

    @abstractmethod
    def update_customer_information_by_id(self, first_name: str, last_name: str, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def get_customer_information_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def create_new_customer(self, first_name: str, last_name: str) -> Customer:
        pass

    @abstractmethod
    def get_all_customers(self) -> list[Customer]:
        pass

    @abstractmethod
    def get_all_accounts(self) -> list[Account]:
        pass

    @abstractmethod
    def get_all_customer_accounts_by_id(self, customer_id: int) -> list[Account]:
        pass
