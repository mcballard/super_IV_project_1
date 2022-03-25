from data_entity_class.row_entity import RowEntity


def test_return_insert_sql_string_success():
    dictionary_for_test = {
        "table_name": "employees",
        "username": "newguy",
        "password": "password",
        "first_name": "jimmy",
        "last_name": "dean"}
    new_employee_str = RowEntity(dictionary_for_test)
    print(new_employee_str)
    assert new_employee_str.return_insert_sql_string() == "insert into project_one_sandbox.employees values " \
                                                          "(default, 'newguy', 'password', 'jimmy', 'dean')" \
                                                          " returning *;"


def test_return_select_sql_string_success():
    dictionary_for_test = {
        "table_name": "reimbursement_requests",
        "employee_id": 1
    }
    total_amount_requests_str = RowEntity(dictionary_for_test)
    total_str = total_amount_requests_str.return_select_sql_string()
    assert total_str == "select sum(amount) as total from project_one_sandbox.reimbursement_requests where employee_id=1;"

def test_return_delete_sql_string_success():
    pass

