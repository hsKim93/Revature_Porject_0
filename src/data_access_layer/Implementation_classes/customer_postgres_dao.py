from src.data_access_layer.Implementation_classes.customer_dao import CustomerDao
from src.entities.account import Account
from src.entities.customer import Customer
from src.util.database_connection import connection


class PlayerPostgresDAO(CustomerDao):

    def create_account(self, customer: Customer, initial_balance: int) -> Account:
        sql = "insert into customer values(%s, %s, %s, default, %s) returning account_id"
        cursor = connection.curosr()
        cursor.execute(sql, ())

        connection.commit()
        pass

    def get_balance_by_id(self, account_id: int) -> int:
        pass

    def deposit_by_id(self, account_id: int, amount: int) -> int:
        pass

    def withdraw_by_id(self, account_id: int, amount: int) -> int:
        pass

    def transfer_by_ids(self, account_id_from: int, account_id_to: int, amount: int) -> bool:
        pass

    def update_customer_information_by_id(self, first_name: str, last_name: str, customer_id: int) -> Customer:
        pass

    def get_customer_information_by_id(self, customer_id: int) -> Customer:
        pass

    def delete_account_by_id(self, account_id: int) -> Account:
        pass

    def delete_customer_by_id(self, customer_id: int) -> Customer:
        pass
