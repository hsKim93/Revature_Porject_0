from src.data_access_layer.Implementation_classes.customer_postgres_dao import CustomerPostgresDao

customer_dao_postgres = CustomerPostgresDao()

def test_create_account():
    created_account = customer_dao_postgres.create_account(2000, 1)
    assert created_account.customer_id == 1 and created_account.balance == 2000

def test_get_balance_by_id():
    result = customer_dao_postgres.get_balance_by_id(1)
    assert result == 5000

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
    updated_customer = customer_dao_postgres.update_customer_information_by_id("Jane", "Doe", 1)
    assert updated_customer.first_name == "Jane" and updated_customer.last_name == "Doe"

# def test_get_customer_information_by_id():
#     result = customer_dao.get_customer_information_by_id(2)
#     assert result.customer_id == 2 and result.last_name == "Kim"
#
# def test_delete_account_by_id():
#     before_deleted = customer_dao.account_list[2]
#     deleted_account = customer_dao.delete_account_by_id(3)
#     assert before_deleted is deleted_account
#
# def test_delete_customer_by_id():
#     before_deleted = customer_dao.customer_list[1]
#     deleted_customer = customer_dao.delete_customer_by_id(2)
#     assert before_deleted is deleted_customer
#
# def test_create_new_customer():
#     pass
#
# def test_get_all_customers():
#     pass
#
# def test_get_all_accounts():
#     pass
#
# def test_get_all_customer_accounts_by_id():
#     pass