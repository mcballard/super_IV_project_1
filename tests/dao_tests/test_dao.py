from Data_access_layer.dao_imp import DAOImp

test_dao = DAOImp()


def test_create_reimbursement_request_success():
    sql_query = "insert into project_one_sandbox.employees " \
                "values (default, 'newguy', 'password', 'jimmy', 'dean') returning *;"
    new_employee = test_dao.create_reimbursement_request(sql_query)
    print(new_employee.row_entity_dict["employee_id"])
    assert new_employee.row_entity_dict["employee_id"] != -1


def test_cancel_reimbursement_request_success():
    pass


def test_select_total_amount_requested_success():
    pass
