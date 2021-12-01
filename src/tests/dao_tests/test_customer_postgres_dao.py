from src.data_access_layer.Implementation_classes.customer_postgres_dao import CustomerPostgresDao

customer_dao_postgres = CustomerPostgresDao()

def test_create_new_customer():
    customer_created = customer_dao_postgres.create_new_customer("New", "Customer")
    assert customer_created.first_name == "New" and customer_created.last_name == "Customer"

def test_get_all_customers():
    all_customers = customer_dao_postgres.get_all_customers()
    assert len(all_customers) > 1

def test_get_all_accounts():
    all_accounts = customer_dao_postgres.get_all_accounts()
    assert len(all_accounts) > 1

def test_get_all_customer_accounts_by_id():
    success = True
    customer_accounts = customer_dao_postgres.get_all_customer_accounts_by_id(1)
    for account in customer_accounts:
        if account.customer_id != 1:
            success = False
    assert success

def test_create_account():
    created_account = customer_dao_postgres.create_new_account(999999999, 1)
    assert created_account.customer_id == 1 and created_account.balance == 999999999

def test_get_balance_by_id():
    result = customer_dao_postgres.get_balance_by_id(3)
    assert result == 50

def test_deposit_by_id():
    balance_before = customer_dao_postgres.get_balance_by_id(1)
    result = customer_dao_postgres.deposit_by_id(1, 500)
    assert result == balance_before + 500

def test_withdraw_by_id():
    balance_before = customer_dao_postgres.get_balance_by_id(1)
    result = customer_dao_postgres.withdraw_by_id(1, 500)
    assert result == balance_before - 500

def test_transfer_by_ids():
    success = customer_dao_postgres.transfer_by_ids(1, 2, 500)
    assert success

def test_update_customer_information_by_id():
    updated_customer = customer_dao_postgres.update_customer_information_by_id("Jane", "Doe", 3)
    assert updated_customer.first_name == "Jane" and updated_customer.last_name == "Doe"

def test_get_customer_information_by_id():
    result = customer_dao_postgres.get_customer_information_by_id(2)
    assert result.customer_id == 2 and result.first_name == "Jonathan" and result.last_name == "Kim"

def test_delete_account_by_id():
    account_for_test = customer_dao_postgres.create_new_account(9999, 1)
    success = customer_dao_postgres.delete_account_by_id(account_for_test.account_id)
    assert success

def test_delete_customer_by_id():
    customer_for_test = customer_dao_postgres.create_new_customer("dummy", "customer")
    success = customer_dao_postgres.delete_customer_by_id(customer_for_test.customer_id)
    assert success

