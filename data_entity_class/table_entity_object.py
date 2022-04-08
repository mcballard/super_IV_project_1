import re
from ast import literal_eval


class TableEntity:
    def __init__(self, new_table_select: dict):
        # dictionary table row looks like in the database where keys are column names
        # and values are the values in the columns
        # the dictionary should include the table name as well
        self.table_entity_dict = new_table_select
        self.dev_db_schema = "project_one_sandbox."

    def return_json_friendly_dictionary(self) -> dict:
        commas = 0
        too_many_commas = 0
        camel_case_dictionary = {}
        dictionary_for_conversion = self.table_entity_dict
        for key in dictionary_for_conversion:
            # regular expression breaks up the key into words starting with _ or .
            # lamda function returns the value with an un uppercase in the group of letters that makes
            # up the word in the spot just after the _ or . then the regular expression removes the _ or .
            # and returns the transformed key string
            camel_case_key = re.sub('_.', lambda words: words.group()[1].upper(), key)
            camel_case_dictionary[camel_case_key] = dictionary_for_conversion[key]
            too_many_commas += 1
        dictionary_concat = "{"
        for key in camel_case_dictionary:
            commas += 1
            dictionary_concat += "'" + str(key) + "':"
            dictionary_concat += "'" + str(camel_case_dictionary[key]) + "'"
            if commas < too_many_commas:
                dictionary_concat += ","
        dictionary_concat += "}"
        return literal_eval(dictionary_concat)

    def return_insert_sql_string(self) -> str:
        pass

    def return_select_sql_string(self) -> str:
        sql_query = "select * from " + self.dev_db_schema + self.table_entity_dict["tableName"] + ";"
        return sql_query

    def return_delete_sql_string(self) -> str:
        pass
