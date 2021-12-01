from src.data_access_layer.abstract_classes.customer_dao_abc import CustomerDaoAbc
from src.entities.account import Account
from src.entities.customer import Customer
from src.util.database_connection import connection


class CustomerPostgresDao(CustomerDaoAbc):
    def create_new_customer(self, first_name: str, last_name: str) -> Customer:
        sql = "insert into customer values(default, %s, %s) returning customer_id, first_name, last_name"
        cursor = connection.cursor()
        cursor.execute(sql, (first_name, last_name))
        connection.commit()
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    def get_all_customers(self) -> list[Customer]:
        sql = "select * from customer"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        customer_record = cursor.fetchall()
        customer_list = []
        for customer in customer_record:
            customer_list.append(Customer(*customer))
        return customer_list

    def get_all_accounts(self) -> list[Account]:
        sql = "select * from account"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        account_record = cursor.fetchall()
        account_list = []
        for account in account_record:
            account_list.append(Account(*account))
        return account_list

    def get_all_customer_accounts_by_id(self, customer_id: int) -> list[Account]:
        sql = "select * from account where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        account_record = cursor.fetchall()
        account_list = []
        for account in account_record:
            account_list.append(Account(*account))
        return account_list

    def create_new_account(self, initial_balance: float, customer_id: int) -> Account:
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
              "returning customer_id, first_name, last_name"
        cursor = connection.cursor()
        cursor.execute(sql, (first_name, last_name, customer_id))
        connection.commit()
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    def get_customer_information_by_id(self, customer_id: int) -> Customer:
        sql = "select * from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    def delete_account_by_id(self, account_id: int) -> bool:
        sql = "delete from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True

    def delete_customer_by_id(self, customer_id: int) -> bool:
        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True
