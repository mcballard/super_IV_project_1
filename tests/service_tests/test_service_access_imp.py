from unittest.mock import MagicMock

from Data_access_layer.dao_imp import DAOImp
from custom_exceptions.failed_transaction import FailedTransaction
from service_access_layer.service_access_imp import ServiceAccessIMP

test_dao = DAOImp()
test_service = ServiceAccessIMP(test_dao)


def test_do_login_success():
    test_login = {
        "tableName": "employees",
        "username": "jb007",
        "password": "shakennotstirred"
    }
    assert test_service.do_login(test_login) == "jb007shakennotstirred1"


def test_do_login_wrong_password():
    try:
        test_login = {
            "tableName": "employees",
            "username": "jb007",
            "password": "thisiswrong"
        }
        test_service.do_login(test_login)
        assert False
    except FailedTransaction as e:
        assert str(e) == "Password is incorrect!"


def test_do_login_wrong_username():
    try:
        test_login = {
            "tableName": "employees",
            "username": "thisiswrong",
            "password": "shakennotstirred"
        }
        test_service.do_login(test_login)
        assert False
    except FailedTransaction as e:
        assert str(e) == "Username is incorrect!"


def test_sanitize_json_from_api_success():
    test_dict = {
        "tableName": "tablename",
        "tableNameId": 1
    }
    assert test_service.sanitize_json_from_api(test_dict)["table_name_id"] == 1


def test_sanitize_json_from_api_non_string_table_name():
    try:
        test_dict = {
            "tableName": 5,
            "tableNameId": 1
        }
        test_service.sanitize_json_from_api(test_dict)
        assert False
    except FailedTransaction as e:
        assert str(e) == "The field containing the table name is in the wrong format, must be a string."


def test_sanitize_json_from_api_convertible_number():
    try:
        test_dict = {
            "tableName": "4",
            "tableNameId": 1
        }
        test_service.sanitize_json_from_api(test_dict)
        assert False
    except FailedTransaction as e:
        assert str(e) == "The table name should not be a number"


def test_sanitize_json_from_api_id_field_non_number():
    try:
        test_dict = {
            "tableName": "tablename",
            "tableNameId": "one"
        }
        test_service.sanitize_json_from_api(test_dict)
        assert False
    except FailedTransaction as e:
        assert str(e) == "The input from the api is not convertible to integer for an id field."


def test_service_create_reimbursement_request_comment_less_than_100():
    try:
        test_dict = {
                     "tableName": "tablename",
                     "employeeId": 4,
                     "reasonId": 5,
                     "amount": 100,
                     "reimbursementRequestComment": "service8910service8910service8910service8910service8910service8910service8910service8910service8910service8910service8910v"}
        service_access_input = ServiceAccessIMP(test_dao)
        service_access_input.service_create_reimbursement_request(test_dict)
        assert False
    except FailedTransaction as e:
        assert str(e) == "test service reimbursement request should not exceed 100"


def test_service_create_reimbursement_request_amount_between_1_and_1000():
    try:
        test_dict = {
                     "tableName": "tablename",
                     "employeeId": 4,
                     "reasonId": 5,
                     "amount": 1000000,
                     "reimbursementRequestComment": "this is ok"}
        test_service.service_create_reimbursement_request(test_dict)
        assert False
    except FailedTransaction as e:
        assert str(e) == "reimbursement amount must be between $1 and $1000"


def test_service_create_reimbursement_request_success():
    new_record = {
        "tableName": "reimbursement_requests",
        "employeeId": 4,
        "reasonId": 2,
        "amount": 100,
        "reimbursementRequestComment": "this is ok"
    }
    test_service.dao_obj.create_reimbursement_request=MagicMock(
            new_record={"tableName": "reimbursement_requests",
                            "employeeId": 4, "reasonId": 2, "amount": 100, "reimbursementRequestComment": "this is ok"})

    assert test_service.service_create_reimbursement_request(new_record).row_entity_dict["reimbursement_request_id"] is not None


def test_service_create_reimbursement_request_catch_amount_non_numeric():
    bad_record = {
        "tableName": "reimbursement_requests",
        "employeeId": 4,
        "reasonId": 2,
        "amount": "Hello there",
        "reimbursementRequestComment": "this is ok"
    }
    try:
        test_service.service_create_reimbursement_request(bad_record)
        assert False
    except FailedTransaction as e:
        assert str(e) == "The amount should be a numeric value"


def test_service_select_total_amount_requested_by_id_success():
    amount_request = {
        "tableName": "reimbursement_requests",
        "employeeId": 4,
        }
    test_service.dao_obj.select_total_amount_requested=MagicMock(return_value=100)
    assert test_service.service_select_total_amount_requested(amount_request) == 100


def test_service_cancel_reimbursement_request_success():
    cancel_request = {
        "tableName": "reimbursement_requests",
        "reimbursementRequestId": 1
    }
    test_service.dao_obj.cancel_reimbursement_request=MagicMock(return_value=True)
    assert test_service.service_cancel_reimbursement_request(cancel_request)

