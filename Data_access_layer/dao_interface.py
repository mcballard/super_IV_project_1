from abc import ABC, abstractmethod

from data_entity_class.row_entity import RowEntity


class ReimbursementInterface(ABC):

    @abstractmethod
    def create_reimbursement_request(self, sql_query: str) -> RowEntity:
        pass

    @abstractmethod
    def cancel_reimbursement_request(self, sql_query: str) -> bool:
        pass

    @abstractmethod
    def select_total_amount_requested(self, sql_query: str) -> float:
        pass

