from abc import ABC, abstractmethod

from data_entity_class.row_entity import RowEntity


class ServiceAccessInterface(ABC):

    @abstractmethod
    def service_create_reimbursement_request(self, entity_dictionary: dict) -> RowEntity:
        pass

    @abstractmethod
    def service_cancel_reimbursement_request(self, entity_dictionary: dict) -> bool:
        pass

    @abstractmethod
    def service_select_total_amount_requested(self, entity_dictionary: dict) -> float:
        pass

