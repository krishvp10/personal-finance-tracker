import db.queries as dq

def add_transaction(conn, category, amount, transaction_type, description, date):
    dq.insert_transaction(conn,category,amount,transaction_type,description,date)
    return "transaction is added succeesfully :)"

def get_transactions(conn):
    transaction=dq.get_all_transactions(conn)
    return transaction

def delete_trans(conn,id):
    dq.delete_transaction(conn,id)
    return "the transaction has been deleted succesfully"

def show_by_type(conn,transaction_type):
    transaction=dq.get_transaction_type(conn,transaction_type)
    return transaction

def show_by_category(conn,category):
    transaction=dq.get_transaction_category(conn,category)
    return transaction

def monthly_summary(conn,month,year):
    income,expense,net=dq.get_monthly_summary(conn,month,year)
    return income,expense,net

def spending_category(conn,month,year):
    result = dq.get_spending_by_category(conn,month,year)
    return result