from Data_access_layer.dao_imp import DAOImp

dao_obj = DAOImp()


def truncate_requests():
    sql_query = "TRUNCATE TABLE project_one_sandbox.reimbursement_requests RESTART IDENTITY CASCADE;"
    dao_obj.trunc_table(sql_query)

truncate_requests()

