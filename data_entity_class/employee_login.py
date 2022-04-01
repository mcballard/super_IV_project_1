from data_entity_class.row_entity import RowEntity


class EmployeeLogin:

    def __init__(self, login_info: dict):
        self.login_info = login_info

    def return_select_sql_string(self) -> str:
        return "select employee_id, username, pass from " \
                    "project_one_sandbox.employees where username='"+self.login_info["username"]+"';"
