
class RowEntity:
    def __init__(self, new_row_entity: dict):
        self.row_entity_dict = new_row_entity
        self.dev_db_schema = "project_one_sandbox."

    def return_json_friendly_dictionary(self) -> dict:
        # will return a dictionary with camelCase keys
        pass

    def return_insert_sql_string(self) -> str:
        # will construct and return an insert statement in sql as a string
        pass

    def return_select_sql_string(self) -> str:
        # will construct and return a select statement in sql as a string
        pass

    def return_delete_sql_string(self) -> str:
        # will construct and return a delete statement in sql as a string
        pass
