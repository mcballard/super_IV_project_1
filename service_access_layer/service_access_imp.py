import re
from collections.abc import Mapping
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
        try:
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
        # receive dictionary from api and perform key transform from camelCase to snake_case
        new_request = self.sanitize_json_from_api(entity_dictionary)
        # perform business case logic
        if len(new_request["reimbursement_request_comment"]) > 100:
            raise FailedTransaction("test service reimbursement request should not exceed 100")
        if (float(new_request["amount"]) < 1) or (float(new_request["amount"]) > 1000):
            raise FailedTransaction("reimbursement amount must be between $1 and $1000")
        # since the api dictionary contained the comment information as well we need to separate it from this dictionary
        # in order to create to separate table entries one for the request itself and one for the comment
        # this is done because the business case required the  reimbursement request table entries be numeric values only
        # this is achieved by creating a separate table for the request comments
        # in order to ensure the reimbursement request control flow does not break we remove the extraneous column information
        # for the request comment and store it in its own dictionary. we will also derive the table name for the row entity
        # from the table name for the reimbursement request
        comment = {
            "reimbursement_request_comment": new_request.pop("reimbursement_request_comment")
        }
        # we now use the new_request dictionary it instantiate a RowEntity for a reimbursement request and call it
        # new_reimbursement_request
        new_reimbursement_request = RowEntity(new_request)
        # using the class functions in the RowEntity we create the sql insert string to be used by pycopg in our data layer
        sql_query_for_reimbursement_request = new_reimbursement_request.return_insert_sql_string()
        # we now create a new record in the database using the sql string created above and call it new_record
        new_record = self.dao_obj.create_reimbursement_request(sql_query_for_reimbursement_request)
        # in order to create a complete reimbursement request comment we need the reimbursement request id from the record
        # we just created so we update the new_comment dictionary with the reimbursement_request_id in the dictionary
        # stored in the object returned from the database.
        new_comment = {
            "table_name": new_request["table_name"].strip("s") + "_comments",
            "reimbursement_request_id": new_record.row_entity_dict["reimbursement_request_id"],
            "reimbursement_request_comment": comment.pop("reimbursement_request_comment")
        }
        # we now create a RowEntity for the reimbursement_request_comment
        new_reimbursement_request_comment = RowEntity(new_comment)
        # we now create an insert sql string to be used by psycopg in our data layer to create the request comment
        sql_query_for_reimbursement_request_comment = new_reimbursement_request_comment.return_insert_sql_string()
        # we now create the new record using our data layer object and the sql string from above
        new_record_for_comment = self.dao_obj.create_reimbursement_request(sql_query_for_reimbursement_request_comment)
        # there were no explicit requirements for displaying any information to the user, so we will return just the
        # new_record in case we implement it later.
        return new_record

    def service_cancel_reimbursement_request(self, entity_dictionary: dict) -> bool:
        cancel_input = self.sanitize_json_from_api(entity_dictionary)
        if type(cancel_input["reimbursement_request_id"]) == int:
            canceled_request = RowEntity(cancel_input)
            sql_query_for_cancel_reimbursement_request = canceled_request.return_delete_sql_string()
            return self.dao_obj.cancel_reimbursement_request(sql_query_for_cancel_reimbursement_request)
        else:
            raise FailedTransaction("Reimbursement Request ID should be numeric!")

    def service_select_total_amount_requested(self, entity_dictionary: dict) -> float:
        select_input = self.sanitize_json_from_api(entity_dictionary)
        if type(select_input["employee_id"]) == int:
            service_select_total_amount = RowEntity(select_input)
            return self.dao_obj.select_total_amount_requested(service_select_total_amount.return_select_sql_string())
        else:
            raise FailedTransaction("test reimbursement employee_id cannot use numeric type")
