from Data_access_layer import dao_interface
from custom_exceptions.failed_transaction import FailedTransaction
from data_entity_class.row_entity import RowEntity
from service_access_layer.service_access_interface import ServiceAccessInterface


class ServiceAccessIMP(ServiceAccessInterface):

    def __init__(self, dao_object: dao_interface):
        self.dao_obj = dao_object

    def service_create_reimbursement_request(self, entity_dictionary: dict) -> RowEntity:
        pass

    def service_cancel_reimbursement_request(self, entity_dictionary: dict) -> bool:
        if type(entity_dictionary["reimbursement_request_id"]) == int:
            return True
        else:
            raise FailedTransaction("Reimbursement Request ID should be numeric!")

    def service_select_total_amount_requested(self, entity_dictionary: dict) -> float:
        pass
