from Data_access_layer.connection_obj import connection
from Data_access_layer.dao_interface import ReimbursementInterface
from custom_exceptions.failed_transaction import FailedTransaction
from data_entity_class.row_entity import RowEntity


class DAOImp(ReimbursementInterface):

    def create_reimbursement_request(self, sql_query: str) -> RowEntity:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        if cursor.rowcount < 1:
            connection.rollback()
            raise FailedTransaction("No record was created, transaction rolled back.")
        else:
            connection.commit()
            new_record_tuple_list = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            mapping = {}
            if len(new_record_tuple_list) != 0:
                for record in new_record_tuple_list:
                    for i in range(len(column_names)):
                        mapping.update({column_names[i]: record[i]})
                    new_record = RowEntity(mapping)
                return new_record
            else:
                raise FailedTransaction("Record may have been created, but no results were returned.")

    def cancel_reimbursement_request(self, sql_query: str) -> bool:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        if cursor.rowcount < 1:
            connection.rollback()
            raise FailedTransaction("No record was deleted, transaction rolled back.")
        else:
            connection.commit()
            return True

    def select_total_amount_requested(self, sql_query: str) -> float:
        cursor = connection.cursor()
        cursor.execute(sql_query)
        if cursor.rowcount < 1:
            connection.rollback()
            raise FailedTransaction("No record was viewed, transaction rolled back.")
        else:
            connection.commit()
            total = cursor.fetchone()[0]
            return total

