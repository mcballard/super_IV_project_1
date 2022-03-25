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
    assert new_employee_str.return_insert_sql_string() == "insert into " \
                                                      "project_one_sandbox.employees " \
                                                      "values (default, 'newguy', 'password', 'jimmy', 'dean') returning *;"


def test_return_select_sql_string_success():
    pass


def test_return_delete_sql_string_success():
    pass

