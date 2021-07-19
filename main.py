from DBconnect import DB
import sqlite3

######################################################


###"""""""""""""""Partie Graine"""""""""""""""###


def main_add_graines(Id, name, category_id, color, quantity, descent, harvest_date, sowing_month, observation):
    
    conn, cursor = DB.connect() 

    try:
        if Id == None:
            cursor.execute("""SELECT ID FROM Graines ;""")
            rows = cursor.fetchall()
            row = rows[-1][0] + 1
        else:
            row = Id

        parameter = """INSERT or IGNORE INTO Graines (ID, Name, Category_Id, Color, Quantity, Descent, Harvest_date, Sowing_month, Observation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) ;"""
        comm = (row, name, category_id, color, quantity, descent, harvest_date, sowing_month, observation)
        cursor.execute(parameter, comm)
        print("seed added")
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()


def main_modif_graines(Id, name, category_id, color, quantity, descent, harvest_date, sowing_month, observation):

    conn, cursor = DB.connect() 

    try:
        parameter = """UPDATE Graines SET Name = ?, Category_Id = ?, Color = ?, Quantity = ?, Descent = ?, Harvest_date = ?, Sowing_month = ?, Observation = ? WHERE ID = ? ;"""        
        comm = (name, category_id, color, quantity, descent, harvest_date, sowing_month, observation, Id)
        cursor.execute(parameter, comm)
        print("seed modified")
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()


def get_seeds_values():       #get Ids, Names, Aver_prices, Max_prices, Dates from the data base

    conn, cursor = DB.connect()

    try:
        cursor.execute("SELECT Graines.ID, Graines.Name, Graines.Color, Graines.Quantity, Category.Name, Graines.Descent, Graines.Harvest_date, Graines.Sowing_month, Graines.Observation FROM Graines INNER JOIN Category ON Graines.Category_Id = Category.ID ;")
        rows = cursor.fetchall()
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()  
    
    return rows   


def del_seed(Id):
    
    conn, cursor = DB.connect()

    try:
        cursor.execute("DELETE FROM Graines WHERE ID = %s ;" % Id)
        print("seed deleted")
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()


###"""""""""""""""Partie Membre"""""""""""""""###


def main_add_member(Id, name, fname, phone, email, city, donation, reception):
        
    conn, cursor = DB.connect() 

    try:
        if Id == None:
            cursor.execute("""SELECT ID FROM Membres ;""")
            rows = cursor.fetchall()
            row = rows[-1][0] + 1
        else:
            row = Id
        parameter = """INSERT or IGNORE INTO Membres (ID, Name, Fname, Phone, Email, City, Donation, Reception) VALUES (?, ?, ?, ?, ?, ?, ?, ?) ;"""
        comm = (row, name, fname, phone, email, city, donation, reception)
        cursor.execute(parameter, comm)
        print("Membre added")

    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()


def main_modif_member(Id, name, fname, phone, email, city, donation, reception):

    conn, cursor = DB.connect() 

    try:
        parameter = """UPDATE Membres SET Name = ?, Fname = ?, Phone = ?, Email = ?, City = ?, Donation = ?, Reception = ? WHERE ID = ? ;"""        
        comm = (name, fname, phone, email, city, donation, reception, Id)
        cursor.execute(parameter, comm)
        print("member modified")
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()


def get_member():
    
    conn, cursor = DB.connect()

    try:
        cursor.execute("SELECT ID, Name, Fname, Phone, Email, City, Donation, Reception FROM Membres ;")
        rows = cursor.fetchall()
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()  
    
    return rows


def del_mem(Id):

    conn, cursor = DB.connect()

    try:
        cursor.execute("DELETE FROM Membres WHERE ID = %s ;" % Id)
        print("member deleted")

    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit() 


###"""""""""""""""Partie Catégorie"""""""""""""""###


def add_category(Id, name):
        
    conn, cursor = DB.connect() 

    try:
        if Id == None:
            cursor.execute("""SELECT ID FROM Category ;""")
            rows = cursor.fetchall()
            row = rows[-1][0] + 1
        else:
            row = Id

        parameter = """INSERT or IGNORE INTO Category (ID, Name) VALUES (?, ?) ;"""
        comm = (row, name)
        cursor.execute(parameter, comm)
        
      
        print("category added")
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()


def get_category(): 
    
    conn, cursor = DB.connect()

    try:
        cursor.execute("SELECT ID, Name FROM Category ;")
        rows = cursor.fetchall()
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()  
    
    return rows   


###"""""""""""""""Partie Transaction"""""""""""""""###


def add_transaction(Id, member_id, seed_id, date, quantity):
    
    conn, cursor = DB.connect() 

    try:
        if Id == None:
            cursor.execute("""SELECT ID FROM Transactions ;""")
            rows = cursor.fetchall()
            row = rows[-1][0] + 1
        else:
            row = Id
        
        parameter = """INSERT or IGNORE INTO Transactions (ID, Member_ID, Seed_ID, Datee, Quantity) VALUES (?, ?, ?, ?, ?) ;"""
        comm = (row, member_id, seed_id, date, quantity)
        cursor.execute(parameter, comm)
        
        cursor.execute("""SELECT Quantity FROM Graines WHERE ID = '%s' ;""" % seed_id)
        rows2 = cursor.fetchall()
        
        new_value = rows2[0][0] + quantity 

        parameter2 = """UPDATE Graines SET Quantity = ? WHERE ID = ? ;"""
        comm2 = (new_value, seed_id)
        cursor.execute(parameter2, comm2)

        if quantity >= 0:
            cursor.execute("""SELECT Donation FROM Membres WHERE ID = '%s' ;""" % member_id)
            rows3 = cursor.fetchall()
            new_value2 = rows3[0][0] + 1
            parameter2 = """UPDATE Membres SET Donation = ? WHERE ID = ? ;"""
            comm2 = (new_value2, seed_id)
            cursor.execute(parameter2, comm2)
        else: 
            cursor.execute("""SELECT Reception FROM Membres WHERE ID = '%s' ;""" % member_id)
            rows3 = cursor.fetchall()
            new_value2 = rows3[0][0] + 1
            parameter2 = """UPDATE Membres SET Reception = ? WHERE ID = ? ;"""
            comm2 = (new_value2, seed_id)
            cursor.execute(parameter2, comm2)

        print("transaction added")

    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()    


def get_transaction():
    
    conn, cursor = DB.connect()

    try:
        cursor.execute("SELECT Transactions.ID, Membres.Name, Graines.Name, Transactions.Quantity, Transactions.Datee FROM Transactions INNER JOIN Membres ON Transactions.Member_ID = Membres.ID INNER JOIN Graines on Transactions.Seed_ID = Graines.ID ;")
        rows = cursor.fetchall()
    
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit()  
    
    return rows

def del_trans(trs):

    conn, cursor = DB.connect()

    try:
        print(trs)
        cursor.execute("""SELECT Seed_ID FROM Transactions WHERE ID = '%s' ;""" % trs[0])
        seed_id = cursor.fetchall()

        cursor.execute("""SELECT Member_ID FROM Transactions WHERE ID = '%s' ;""" % trs[0])
        member_id = cursor.fetchall()

        cursor.execute("""SELECT Quantity FROM Graines WHERE ID = '%s' ;""" % seed_id[0][0])
        qte_seed = cursor.fetchall()
        
        new_value = qte_seed[0][0] - int(trs[3])

        parameter = """UPDATE Graines SET Quantity = ? WHERE ID = ? ;"""
        comm = (new_value, seed_id[0][0])
        cursor.execute(parameter, comm)

        if int(trs[3]) >= 0:
            cursor.execute("""SELECT Donation FROM Membres WHERE ID = '%s' ;""" % member_id[0][0])
            rows3 = cursor.fetchall()
            new_value2 = rows3[0][0] - 1
            parameter2 = """UPDATE Membres SET Donation = ? WHERE ID = ? ;"""
            comm2 = (new_value2, seed_id[0][0])
            cursor.execute(parameter2, comm2)
        else: 
            cursor.execute("""SELECT Reception FROM Membres WHERE ID = '%s' ;""" % member_id[0][0])
            rows3 = cursor.fetchall()
            new_value2 = rows3[0][0] - 1
            parameter2 = """UPDATE Membres SET Reception = ? WHERE ID = ? ;"""
            comm2 = (new_value2, seed_id[0][0])
            cursor.execute(parameter2, comm2)
        
        cursor.execute("DELETE FROM Transactions WHERE ID = %s ;" % trs[0])
        print("transactions deleted")

    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    conn.commit() 



######################################################

#get_seeds_values()    
#[(0, 'coucourge', 'orange avec des points noirs', 21, 0, None, '2021', 'en mai', 'elles ne sont en fait pas orange mais bleu'), (1, 'popotirond', 'vert claire', 35, 1, 7, '2020', 'en juin', 'pas mal en soupe')]
#main_modif_graines(2, "poti", 1, "vert", 12, 6, 123, "dfgh", "sdfgsdfgsdfg")
#add_member(None ,"Didou", 2, 5)
#del_seed(104)
#add_category(None , "Carottes")
#add_transaction(None , 1, 1, "10/05/2021", 5)
#print(len(get_category()))
#print(get_member())
#print(get_transaction())
#del_trans(8)