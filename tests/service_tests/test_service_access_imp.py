import service_access_layer
from Data_access_layer.dao_imp import DAOImp
from custom_exceptions.failed_transaction import FailedTransaction
from data_entity_class.row_entity import RowEntity
from service_access_layer.service_access_imp import ServiceAccessIMP

test_dao = DAOImp()


def test_service_create_reimbursement_request_comment_less_than_100():
    try:
        service_access_input = ServiceAccessIMP(test_dao)
        service_access_input_test_entity = {
           "request_comment": 'service8910service8910service8910service8910service8910service8910service8910service8910service8910service8910service8910v'}
        service_access_input.service_create_reimbursement_request(service_access_input_test_entity)
        assert False
    except FailedTransaction as e:
        assert str(e) == "test service reimbursement request should not exceed 100"


def test_service_create_reimbursement_request_amount_between_1_and_1000():
    pass


def test_service_create_reimbursement_request_success():
    pass


def test_service_cancel_reimbursement_request_id_is_not_a_number():
    pass


def test_service_cancel_reimbursement_request_success():
    pass


def test_service_select_total_amount_requested_employee_id_non_numeric():
    pass


def test_service_select_total_amount_requested_employee_id_success():
    pass
