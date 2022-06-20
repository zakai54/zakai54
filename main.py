import sqlite3

con = sqlite3.connect("supermarket.db")
cursor = con.cursor()


def adminLoginWindow():
    print("=====================")
    print("1.Display products")
    print("2.Add Product")
    print("3.Remove Product")
    print("4.search for product")
    print("5 to update product value in Grocery ")
    print("6 to update product value in Gadgets ")
    print("7.logout")
    print("=====================")


def searchbyid():
    search = int(input("enter 1 to search in grocery or 2 to search in Gadgets : "))
    if search == 1:
        search_id = input("enter product id : ")
        run = cursor.execute('''SELECT * from Grocery WHERE id = ? ''', (search_id,))
        print("====================================================")
        for i in run:
            print(i)

    elif search == 2:
        search_id = input("enter product id : ")
        run = cursor.execute('''SELECT * from Gadgets WHERE id = ? ''', (search_id,))
        print("====================================================")
        for i in run:
            print(i)
    elif ():
        print("invalid id")


def updatevaluegrocery():
    user_choice = int(input("Enter 1 to update name /////// 2 to update quantity ////// 3 to update price  : "))

    if user_choice == 1:
        new_name = input("enter new name : ")
        product_id = int(input("enter id of product : "))
        try:
            cursor.execute('''update Grocery set name =? where id =?''', (new_name, product_id))
            print("record updated successfully")

        except sqlite3.Error as error:
            print("Failed to update record in Grocery", error)

    if user_choice == 2:
        new_quantity = input("enter new quantity : ")
        product_id = int(input("enter id of product : "))
        try:
            cursor.execute('''update Grocery set name =? where id =?''', (new_quantity, product_id))
            print("record updated successfully")

        except sqlite3.Error as error:
            print("Failed to update record in Grocery", error)

    if user_choice == 3:
        new_price = input("enter new price : ")
        product_id = int(input("enter id of product : "))
        try:
            cursor.execute('''update Grocery set name =? where id =?''', (new_price, product_id))
            print("record updated successfully")

        except sqlite3.Error as error:
            print("Failed to update record in Grocery", error)


def updatevaluegadgets():
    user_choice = int(input("Enter 1 to update name /////// 2 to update quantity ////// 3 to update price  : "))

    if user_choice == 1:
        new_name = input("enter new name : ")
        product_id = int(input("enter id of product : "))
        try:
            cursor.execute('''update Gadgets set name =? where id =?''', (new_name, product_id))
            print("record updated successfully")

        except sqlite3.Error as error:
            print("Failed to update record in Gadgets", error)

    if user_choice == 2:
        new_quantity = input("enter new quantity : ")
        product_id = int(input("enter id of product : "))
        try:
            cursor.execute('''update Gadgets set name =? where id =?''', (new_quantity, product_id))
            print("record updated successfully")

        except sqlite3.Error as error:
            print("Failed to update record in Gadgets", error)

    if user_choice == 3:
        new_price = input("enter new price : ")
        product_id = int(input("enter id of product : "))
        try:
            cursor.execute('''update Gadgets set name =? where id =?''', (new_price, product_id))
            print("record updated successfully")

        except sqlite3.Error as error:
            print("Failed to update record in Gadgets", error)


def adminDisplayMenuWindow():
    print("====================================================")
    print("Id\tName\tAvailable\tPrice\t")

    con.commit()
    records = cursor.execute('''select * from Grocery''')
    for i in records:
        print(i)

    con.commit()
    records = cursor.execute('''select * from Gadgets''')
    print("====================================================")
    print("Id\tName\tAvailable\tPrice\t")
    for i in records:
        print(i)


def addproducts():
    choice = int(input("enter 1 to add to grocery or 2 to add to gadgets :  "))
    if choice == 1:
        try:
            print("Enter item in [(id,name,quantity,price)] format below ")
            new_id = int(input('enter id : '))
            new_name = input('enter name : ')
            new_quantity = int(input('quantity : '))
            new_price = int(input('price : '))
            new_item = new_id, new_name, new_price, new_quantity
            cursor.execute(f'''INSERT INTO  Grocery VALUES(?,?,?,?) ''', (new_id, new_name, new_quantity, new_price))
            con.commit()
            records = cursor.execute('''select * from Grocery''')
            for i in records:
                print(i)

        except sqlite3.Error as error:
            print("Failed to add record to Grocery", error)

    if choice == 2:
        try:
            n_id = int(input('enter id : '))
            n_name = input('enter name : ')
            n_quantity = int(input('quantity : '))
            n_price = int(input('price : '))
            new_item = n_id, n_name, n_price, n_quantity
            cursor.execute(f'''INSERT INTO  Gadgets VALUES(?,?,?,?) ''',
                           (n_id, n_name, n_quantity, n_price))
            con.commit()
            records = cursor.execute('''select * from Gadgets''')
            for i in records:
                print(i)
        except sqlite3.Error as error:
            print("Failed to add record to Grocery", error)

    adminDisplayMenuWindow()


def removeproducts():
    nit = int(input("enter 1 to delete from grocery or 2 to delete from gadgets"))
    if nit == 1:

        try:
            value_id = int(input("enter id of product :"))
            cursor.execute('''DELETE from Grocery where id=?''', (value_id,))
            print("Record deleted successfully ")


        except sqlite3.Error as error:
            print("Failed to delete record from Grocery", error)

    if nit == 2:

        try:
            nt_id = input("enter id of product :")
            cursor.execute('''DELETE from Gadgets where id=?''', (nt_id,))
            print("Record deleted successfully ")


        except sqlite3.Error as error:
            print("Failed to delete record from Gadgets", error)

    else:
        print("invalid entry")
        adminDisplayMenuWindow()


def logoutwindow():
    login()


def adminOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 2:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        addproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()
    elif choice == 3:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        removeproducts()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()

    elif choice == 4:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        searchbyid()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()

    elif choice == 5:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        updatevaluegrocery()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()

    elif choice == 6:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        updatevaluegadgets()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()

    elif choice == 7:
        logoutwindow()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions()


def login():
    user_name = input("enter username : ")
    if user_name == 'admin':
        password = input("Enter the password : ")

        if password == "zaramart1":
            adminLoginWindow()
            adminOptions()
        else:
            print("Invalid password. Please enter valid password")
            login()


login()
