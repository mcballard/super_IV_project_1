from abc import ABC, abstractmethod


class ReimbursementInterface(ABC):

    @abstractmethod
    def log_in(self, username, password):
        pass

    @abstractmethod
    def create_reimbursement_request(self, requested_amount, reimbursement_type, short_comment):
        pass

    @abstractmethod
    def cancel_reimbursement_request(self, request_id):
        pass

    @abstractmethod
    def view_total_amount_requested(self):
        pass

    @abstractmethod
    def log_out(self):
        pass

