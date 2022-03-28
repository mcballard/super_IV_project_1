squfrom Data_access_layer.dao_imp import DAOImp

test_dao = DAOImp()


def test_create_reimbursement_request_success():
    sql_query = "insert into project_one_sandbox.employees " \
                "values (default, 'newguy', 'password', 'jimmy', 'dean') returning *;"
    new_employee = test_dao.create_reimbursement_request(sql_query)
    print(new_employee.row_entity_dict["employee_id"])
    assert new_employee.row_entity_dict["employee_id"] != -1


def test_cancel_reimbursement_request_success():
    # may mock later so it passes, can change id to existing record otherwise
    sql_query = "delete from project_one_sandbox.employees where employee_id = 22;"
    return_value = test_dao.cancel_reimbursement_request(sql_query)
    assert return_value


def test_select_total_amount_requested_success():
    sql_query = "select sum(employee_id) as total from project_one_sandbox.employees;"
    total_amount = test_dao.select_total_amount_requested(sql_query)
    print(total_amount)
    assert total_amount != 0

