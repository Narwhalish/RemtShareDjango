import sqlite3

def create_connection(database):
    connection = sqlite3.connect(database)
    return connection

def add_house(house):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO houses (House, Seller, Location, Price, Size) VALUES (?,?,?,?,?)",(house[0],house[1],house[2],house[3],house[4]))
    
    connection.commit()
    connection.close()
    
def add_user(user):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (ID, Username, Password, Email, Associated Houses) VALUES (?,?,?,?,?)",(user[0], user[1], user[2], user[3], user[4]))
    
    connection.commit()
    connection.close()

def edit_user_information():
    return 'null'
    
def edit_house_information():
    return 'null'

def get_user_information(id_number):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE Username = ?',(id_number,))
    information = cursor.fetchall()
    print information
    
    connection.close()

def get_houses_by_seller(seller):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT (House) FROM houses WHERE Seller=?',(seller,))
    information = cursor.fetchall()
    print information
    
    connection.close()