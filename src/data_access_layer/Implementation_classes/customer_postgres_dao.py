from src.data_access_layer.abstract_classes.customer_dao_abc import CustomerDaoAbc
from src.entities.account import Account
from src.entities.customer import Customer
from src.util.database_connection import connection


class CustomerPostgresDao(CustomerDaoAbc):
    def create_account(self, initial_balance: float, customer_id: int) -> Account:
        sql = "insert into account values(default, %s, %s) returning account_id, balance, customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (initial_balance, customer_id))
        connection.commit()
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account

    def get_balance_by_id(self, account_id: int) -> float:
        sql = "select balance from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        balance = cursor.fetchone()[0]
        return balance

    def deposit_by_id(self, account_id: int, amount: float) -> float:
        sql = "update account set balance = balance + %s where account_id = %s returning balance"
        cursor = connection.cursor()
        cursor.execute(sql, (amount, account_id))
        connection.commit()
        balance = cursor.fetchone()[0]
        return balance

    def withdraw_by_id(self, account_id: int, amount: float) -> float:
        sql = "update account set balance = balance - %s where account_id = %s returning balance"
        cursor = connection.cursor()
        cursor.execute(sql, (amount, account_id))
        connection.commit()
        balance = cursor.fetchone()[0]
        return balance

    def transfer_by_ids(self, account_id_from: int, account_id_to: int, amount: float) -> bool:
        sql = "update account set balance = balance - %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (amount, account_id_from))
        sql = "update account set balance = balance + %s where account_id = %s"
        cursor.execute(sql, (amount, account_id_to))
        connection.commit()
        return True

    def update_customer_information_by_id(self, first_name: str, last_name: str, customer_id: int) -> Customer:
        sql = "update customer set first_name = %s, last_name = %s where customer_id = %s " \
              "returning first_name, last_name, customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (first_name, last_name, customer_id))
        connection.commit()
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)


    def get_customer_information_by_id(self, customer_id: int) -> Customer:
        pass

    def delete_account_by_id(self, account_id: int) -> Account:
        pass

    def delete_customer_by_id(self, customer_id: int) -> Customer:
        pass

    def create_new_customer(self, first_name: str, last_name: str) -> Customer:
        pass

    def get_all_customers(self) -> list[Customer]:
        pass

    def get_all_accounts(self) -> list[Account]:
        pass

    def get_all_customer_accounts_by_id(self, customer_id: int) -> list[Account]:
        pass
