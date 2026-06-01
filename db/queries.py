def insert_transaction(conn,category,amount,type,description,date):
    cursor = conn.cursor()
    cat = category.lower()
    amt = float(amount)
    desc = description.lower()
    typ = type.lower()
    cursor.execute("INSERT INTO transactions (category, amount, type, description, date) VALUES (%s, %s, %s, %s, %s)",
                   (cat, amt, typ, desc, date))
    conn.commit()
    cursor.close()

def get_all_transactions(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    cursor.close()
    return transactions    

def delete_transaction(conn,transaction_id):
    curr = conn.cursor()
    curr.execute("DELETE FROM transactions WHERE ID = %s",(transaction_id,))
    conn.commit()
    curr.close()

def get_transaction_type(conn,transaction_type):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE type = %s",(transaction_type,))
    transaction = cursor.fetchall()
    cursor.close()
    return transaction

def get_transaction_category(conn,category):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE category = %s",(category,))
    transaction = cursor.fetchall()
    cursor.close()
    return transaction    

def get_monthly_summary(conn,month,year):
    cursor = conn.cursor()
    cursor.execute("SELECT type, SUM(amount) FROM transactions WHERE EXTRACT(MONTH FROM date) = %s AND EXTRACT(YEAR FROM date) = %s GROUP BY type ORDER BY type",(month,year))
    result = cursor.fetchall()
    income = 0
    expense = 0
    for i in result:
        if i[0] == 'income':
            income = i[1]
        else:
            expense = i[1]
    net = income - expense
    cursor.close()
    return income,expense,net      

def get_spending_by_category(conn, month, year):
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type = 'expense' AND EXTRACT(MONTH FROM date) = %s AND EXTRACT(YEAR FROM date) = %s GROUP BY category ORDER BY category",(month,year)) 
    result= cursor.fetchall()
    cursor.close()
    return result