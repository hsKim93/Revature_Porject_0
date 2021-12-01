from src.custom_exceptions.invalid_request_exception import InvalidRequestException
from src.data_access_layer.Implementation_classes.customer_postgres_dao import CustomerPostgresDao
from src.service_layer.service_imp.customer_postgres_service import CustomerPostgresService

customer_dao = CustomerPostgresDao()
customer_service = CustomerPostgresService(customer_dao)

def test_service_deposit_by_id():
    try:
        customer_service.service_deposit_by_id(1, -200)
    except InvalidRequestException as e:
        assert str(e) == "Amount must be greater than 0"

def test_service_withdraw_by_id_overdraft():
    try:
        customer_service.service_withdraw_by_id(1, 50000)
    except InvalidRequestException as e:
        assert str(e) == "You cannot withdraw more than what you have"

def test_service_withdraw_by_id_negative_amount():
    try:
        customer_service.service_withdraw_by_id(1, -500)
    except InvalidRequestException as e:
        assert str(e) == "Amount must be greater than 0"

def test_service_transfer_by_ids_overdraft():
    try:
        customer_service.service_transfer_by_ids(1, 2, 50000)
    except InvalidRequestException as e:
        assert str(e) == "You cannot transfer more than what you have"

def test_service_transfer_by_ids_negative_amount():
    try:
        customer_service.service_transfer_by_ids(1, 2, -500)
    except InvalidRequestException as e:
        assert str(e) == "Amount must be greater than 0"
