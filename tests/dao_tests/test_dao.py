from Data_access_layer.dao_imp import DAOImp

test_dao = DAOImp()


def test_select_record_success():
    sql_query = "select employee_id, username, pass from " \
                    "project_one_sandbox.employees where username='jb007'"
    login = test_dao.select_record(sql_query)
    assert login.row_entity_dict["username"] == "jb007"


def test_create_db_record():
    sql_query = "insert into project_one_sandbox.employees " \
                "values (default, 'testuser', 'testpass', 'first', 'last') returning *;"
    new_employee = test_dao.create_reimbursement_request(sql_query)
    assert new_employee.row_entity_dict["employee_id"] != -1


def test_delete_db_record():
    last_emp_created_during_tests = test_dao.select_record("select max(employee_id) as employee_id from project_one_sandbox.employees;")
    sql_query = "delete from project_one_sandbox.employees " \
                "where employee_id="+str(last_emp_created_during_tests.row_entity_dict["employee_id"])+";"
    return_value = test_dao.cancel_reimbursement_request(sql_query)
    assert return_value


def test_select_total_amount_requested_success():
    sql_query = "select sum(employee_id) as total from project_one_sandbox.employees;"
    total_amount = test_dao.select_total_amount_requested(sql_query)
    assert total_amount != 0

