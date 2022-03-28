from Data_access_layer import dao_interface
from Data_access_layer.dao_interface import ReimbursementInterface
from custom_exceptions.failed_transaction import FailedTransaction
from data_entity_class.row_entity import RowEntity
from service_access_layer.service_access_interface import ServiceAccessInterface


class ServiceAccessIMP(ServiceAccessInterface):
    def __init__(self, dao_object: ReimbursementInterface):
        self.dao_object = dao_object

    def service_create_reimbursement_request(self, entity_dictionary: dict) -> RowEntity:
        if len(entity_dictionary["request_comment"]) > 100:
            raise FailedTransaction("test service reimbursement request should not exceed 100")


    def service_cancel_reimbursement_request(self, entity_dictionary: dict) -> bool:
        pass

    def service_select_total_amount_requested(self, entity_dictionary: dict) -> float:
        pass
