from abc import ABC, abstractmethod


class ReimbursementInterface(ABC):

    @abstractmethod
    def log_in(self):
        pass

    @abstractmethod
    def create_reimbursement_request(self):
        pass

    @abstractmethod
    def cancel_reimbursement_request(self):
        pass

    @abstractmethod
    def view_total_amount_requested(self):
        pass

    @abstractmethod
    def log_out(self):
        pass