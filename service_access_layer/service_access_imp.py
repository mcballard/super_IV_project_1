from data_entity_class.row_entity import RowEntity
from service_access_layer.service_access_interface import ServiceAccessInterface


class ServiceAccessIMP(ServiceAccessInterface):

    def service_create_reimbursement_request(self, entity_dictionary: dict) -> RowEntity:
        pass

    def service_cancel_reimbursement_request(self, entity_dictionary: dict) -> bool:
        pass

    def service_select_total_amount_requested(self, entity_dictionary: dict) -> float:
        pass
