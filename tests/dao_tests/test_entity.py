from data_entity_class.employee_login import EmployeeLogin
from data_entity_class.row_entity import RowEntity


def test_return_select_sql_string():
    test_dictionary = {
        "table_name": "employees",
        "username": "jb007"
    }
    login_info_string = EmployeeLogin(test_dictionary)
    assert login_info_string.return_select_sql_string() == "select employee_id, username, pass from " \
                                                           "project_one_sandbox.employees where username='jb007';"


def test_return_insert_sql_string_success():
    dictionary_for_test = {
        "table_name": "employees",
        "username": "newguy",
        "password": "password",
        "first_name": "jimmy",
        "last_name": "dean"}
    new_employee_str = RowEntity(dictionary_for_test)
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
    delete = {
        "table_name": "reimbursement_requests",
        "reimbursement_request_id": 1,
    }
    test_delete = RowEntity(delete)
    test_string = test_delete.return_delete_sql_string()
    assert test_string == "delete from project_one_sandbox.reimbursement_requests where reimbursement_request_id=1;"


def test_return_json_friendly_dictionary():
    test_dict = {
        "this_is_snake_case": "something"
    }
    test_ent = RowEntity(test_dict)
    result_dict = test_ent.return_json_friendly_dictionary()
    assert result_dict["thisIsSnakeCase"] == "something"




