

def test_service_create_reimbursement_request_comment_less_than_100():
    pass


def test_service_create_reimbursement_request_amount_between_1_and_1000():
    pass


def test_service_create_reimbursement_request_success():
    pass


def test_service_cancel_reimbursement_request_id_is_not_a_number():
    pass


def test_service_cancel_reimbursement_request_success():
    pass


def test_service_select_total_amount_requested_employee_id_non_numeric():
    try:
        service_access_input = ServiceAccessIMP(test_dao)
        service_access_input_test_employee_id_non_numeric = {"request_employee_id": '345676765432'}
        test_entity = RowEntity(service_access_input_test_employee_id_non_numeric)
        tests.service_tests.service_access_input_test_employee_id_non_numeric
        assert False
    except FailedTransaction as e:
        assert str(e) == "test reimbursement employee_id cannot use numeric type"


def test_service_select_total_amount_requested_employee_id_success():
    pass
