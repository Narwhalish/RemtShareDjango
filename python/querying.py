import sqlite3
from sqlite3 import Error

def create_connection(database):
    try:
        connection = sqlite3.connect(database)
        return connection
    except Error as error:
        print error
    
    return None

def add_house(house):
    connection = create_connection('houses.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO houses (House, Seller, Location, Price, Size) VALUES ({ID},{seller},{location},{price},{size})".\
            format(ID = house[0], seller = house[1], location = house[2], price = house[3], size = house[4]))
    
    connection.commit()
    connection.close()
    
def add_user(user):
    connection = create_connection('users.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (ID, Username, Password, Email, Associated Houses) VALUES ({ID},{username},{password},{email},{lst})".\
            format(ID = user[0], username = user[1], password = user[2], email = user[3], lst = user[4]))
    
    connection.commit()
    connection.close()

def get_user_information(id_number):
    connection = create_connection('users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE ID = {idn}'.format(idn=id_number))
    information = cursor.fetchall()
    print information
    
    connection.close()

def get_houses_by_seller(seller):
    connection = create_connection('users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT (House) FROM houses WHERE Seller={s}'.format(s = seller))
    information = cursor.fetchall()
    print information
    
    connection.close()