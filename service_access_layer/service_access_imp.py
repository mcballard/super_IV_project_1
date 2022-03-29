import re
from re import sub

from Data_access_layer import dao_interface


from custom_exceptions.failed_transaction import FailedTransaction
from data_entity_class.row_entity import RowEntity
from service_access_layer.service_access_interface import ServiceAccessInterface


class ServiceAccessIMP(ServiceAccessInterface):

    def __init__(self, dao_object: dao_interface):
        self.dao_obj = dao_object

    def sanitize_json_from_api(self, json_from_api: dict) -> dict:
        # this will change keys to snake_case and ensure they match database column names
        # this will also ensure number strings are convertible to the appropriate datatypes (i.e. ids are not words)
        # utilize regular expressions to parse the keys
        snake_case_dictionary = {}
        for key in json_from_api:
            snake_key = '_'.join(
                sub('([A-Z][a-z]+)', r' \1', sub('([A-Z]+)', r' \1', key.replace('-', ' '))).split()).lower()
            snake_case_dictionary[snake_key] = json_from_api[key]
        # application specific search for keys with _id should be implemented here including for checks
        # on any other number type expected key, value pairs to ensure values are convertible types
        for key in snake_case_dictionary:
            if re.search("_id", key):
                try:
                    proper_int_format = int(snake_case_dictionary[key])
                    snake_case_dictionary[key] = proper_int_format
                except ValueError as e:
                    raise FailedTransaction("The input from the api is not convertible to integer for an id field.")
        if type(snake_case_dictionary["table_name"]) is not str:
            raise FailedTransaction("The field containing the table name is in the wrong format, must be a string.")
        # the following regular expression should be used on any string value entering the db to prevent sql injection
        snake_case_dictionary["table_name"] = re.sub("[^A-Za-z_0-9]", "", snake_case_dictionary["table_name"])
        try: # check to see if table name is convertible to an integer or in other words is just a number in string form
            check_for_int_as_table_name = int(snake_case_dictionary["table_name"])
            if type(check_for_int_as_table_name) is int:
                raise FailedTransaction("The table name should not be a number")
            check_for_float_as_table_name = float(snake_case_dictionary["table_name"])
            if type(check_for_float_as_table_name) is float:
                raise FailedTransaction("The table name should not be a number")
        except ValueError as e:
            # confirms cannot convert and is not a number normal execution should continue
            if e is ValueError:
                return snake_case_dictionary
        return snake_case_dictionary

    def service_create_reimbursement_request(self, entity_dictionary: dict) -> RowEntity:
        if len(entity_dictionary["request_comment"]) > 100:
            raise FailedTransaction("test service reimbursement request should not exceed 100")

    def service_cancel_reimbursement_request(self, entity_dictionary: dict) -> bool:
        if type(entity_dictionary["reimbursement_request_id"]) == int:
            return True
        else:
            raise FailedTransaction("Reimbursement Request ID should be numeric!")

    def service_select_total_amount_requested(self, entity_dictionary: dict) -> float:
        if type(entity_dictionary["employee_id"]) == int:
            pass
        else:
            raise FailedTransaction("test reimbursement employee_id cannot use numeric type")
