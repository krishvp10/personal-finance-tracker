import services.finance as sf
import db.connection as dc
choice = 0
while choice != 8: 
    print("1. Add Transaction")
    print("2. View All Transactions")
    print("3. View by Type (income/expense)")
    print("4. View by Category")
    print("5. Delete a Transaction")
    print("6. Monthly Summary")
    print("7. Spending by Category")
    print("8. Exit")
    choice = int(input("enter the function you need to perform :"))
 
    if choice == 1:
        category = input("enter the category of the transaction :")
        amount = input("enter the amount of the transaction :")
        transaction_type = input("enter the type of the transaction (income/expense) :")
        description = input("enter a description for the transaction :")
        date = input("enter the date of the transaction (YYYY-MM-DD) :")
        conn = dc.get_connection()
        print(sf.add_transaction(conn, category, amount, transaction_type, description, date))
        conn.close()

    elif choice == 2:
        conn = dc.get_connection()
        transactions = sf.get_transactions(conn)
        for t in transactions:
            print(t)
        conn.close()

    elif choice == 3:
        transaction_type = input("enter the type of transactions to view (income/expense) :")
        conn = dc.get_connection()
        transactions = sf.show_by_type(conn,transaction_type)
        for t in transactions:
            print(t)
        conn.close()

    elif choice == 4:
        category = input("enter the category of transactions to view :")
        conn = dc.get_connection()
        transactions = sf.show_by_category(conn,category)
        for t in transactions:
            print(t)
        conn.close()

    elif choice == 5:
        transaction_id = int(input("enter the ID of the transaction to delete :"))
        conn = dc.get_connection()
        print(sf.delete_trans(conn, transaction_id))
        conn.close()

    elif choice == 6:
        month = int(input("enter the month for the summary (1-12) :"))
        year = int(input("enter the year for the summary (YYYY) :"))
        conn = dc.get_connection()
        income,expense,net = sf.monthly_summary(conn,month,year)
        print(f"Income: {income}, Expense: {expense}, Net: {net}")
        conn.close()

    elif choice == 7:
        month = int(input("enter the month for the spending by category (1-12) :"))
        year = int(input("enter the year for the spending by category (YYYY) :"))
        conn = dc.get_connection()
        result = sf.spending_category(conn,month,year)
        for r in result:
            print(f"Category: {r[0]}, Amount: {r[1]}")
        conn.close()
    elif choice == 8:
        print("Exiting the program.")

    else:
        print("Invalid choice. Please try again.")