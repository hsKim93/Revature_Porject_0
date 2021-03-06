from flask import Flask, request, jsonify

from src.custom_exceptions.invalid_request_exception import InvalidRequestException
from src.data_access_layer.Implementation_classes.customer_postgres_dao import CustomerPostgresDao
from src.service_layer.service_imp.customer_postgres_service import CustomerPostgresService
# import logging
#
# logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)

customer_dao = CustomerPostgresDao()
customer_service = CustomerPostgresService(customer_dao)

@app.post("/customer")
def create_new_customer():
    data = request.get_json()
    customer_result = customer_service.service_create_new_customer(data["firstName"], data["lastName"])
    return jsonify(customer_result.make_dictionary()), 201


@app.get("/customer")
def get_all_customers():
    customer_list = customer_service.service_get_all_customers()
    result_list = []
    for customer in customer_list:
        result_list.append(customer.make_dictionary())
    result_dict = {
        "customers": result_list
    }
    return jsonify(result_dict)

@app.get("/account")
def get_all_accounts():
    account_list = customer_service.service_get_all_accounts()
    result_list = []
    for account in account_list:
        result_list.append(account.make_dictionary())
    result_dict = {
        "accounts": result_list
    }
    return jsonify(result_dict)

@app.get("/customer/<customer_id>/account")
def get_all_customers_accounts_by_id(customer_id: str):
    account_list = customer_service.service_get_all_customer_accounts_by_id(int(customer_id))
    result_list = []
    for account in account_list:
        result_list.append(account.make_dictionary())
    result_dict = {
        "accounts": result_list
    }
    return jsonify(result_dict)

@app.post("/customer/account")
def create_new_account():
    data = request.get_json()
    account_result = customer_service.service_create_new_account(data["balance"], data["customerId"])
    return jsonify(account_result.make_dictionary()), 201


@app.get("/customer/account/<account_id>")
def get_balance_by_id(account_id: str):
    balance = customer_service.service_get_balance_by_id(int(account_id))
    balance_dict = {
        "balance": balance
    }
    return jsonify(balance_dict), 200


@app.put("/customer/account/<account_id>/deposit")
def deposit_by_id(account_id: str):
    try:
        data = request.get_json()
        amount = data["amount"]
        balance = customer_service.service_deposit_by_id(int(account_id), amount)
        result_dict = {
            "deposit amount": amount,
            "remaining balance": balance
        }
        return jsonify(result_dict), 200
    except InvalidRequestException as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400


@app.put("/customer/account/<account_id>/withdraw")
def withdraw_by_id(account_id: str):
    try:
        data = request.get_json()
        amount = data["amount"]
        balance = customer_service.service_withdraw_by_id(int(account_id), amount)
        result_dict = {
            "withdraw amount": amount,
            "remaining balance": balance
        }
        return jsonify(result_dict), 200
    except InvalidRequestException as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400


@app.put("/customer/account/<account_id_from>/transfer")
def transfer_by_ids(account_id_from: str):
    try:
        data = request.get_json()
        amount = data["amount"]
        account_id_to = data["accountIdTo"]
        success = customer_service.service_transfer_by_ids(int(account_id_from), account_id_to, amount)
        if success:
            result_dict = {
                "message": "Transferred Successfully"
            }
            return jsonify(result_dict), 200
        else:
            result_dict = {
                "message": "Transfer failed"
            }
            return jsonify(result_dict), 400
    except InvalidRequestException as e:
        error_message = {
            "errorMessage": str(e)
        }
        return jsonify(error_message), 400


@app.put("/customer/<customer_id>")
def update_customer_information_by_id(customer_id: str):
    data = request.get_json()
    first_name = data["firstName"]
    last_name = data["lastName"]
    updated_customer = customer_service.service_update_customer_information_by_id(first_name,
                                                                                  last_name, int(customer_id))
    return jsonify(updated_customer.make_dictionary()), 200


@app.get("/customer/<customer_id>")
def get_customer_information_by_id(customer_id: str):
    customer_result = customer_service.service_get_customer_information_by_id(int(customer_id))
    return jsonify(customer_result.make_dictionary()), 200


@app.delete("/customer/account/<account_id>")
def delete_account_by_id(account_id: str):
    customer_service.service_delete_account_by_id(int(account_id))
    return_message = {
        "message": "Successfully deleted account with id " + account_id
    }
    return jsonify(return_message), 200


@app.delete("/customer/<customer_id>")
def delete_customer_information_by_id(customer_id: str):
    customer_service.service_delete_customer_by_id(int(customer_id))
    return_message = {
        "message": "Successfully deleted customer with id " + customer_id
    }
    return jsonify(return_message), 200

app.run()
