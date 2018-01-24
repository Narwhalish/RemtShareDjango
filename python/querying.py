import sqlite3

def create_connection(database):
    connection = sqlite3.connect(database)
    return connection

def login(username, password):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT Password FROM users WHERE Username = ?',(username,))
    passwords = cursor.fetchall()
    
    for word in passwords:
        if word[0] == password:
            cursor.execute('SELECT * FROM users WHERE Username = ? AND Password = ?',(username,password))
            user_information = cursor.fetchall()
            return user_information
        
    connection.close()
    
    return False

def get_all_houses():
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT House FROM HousesForSale')
    information = cursor.fetchall()
    
    connection.close()
    
    return information

def get_house_information(house_id):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM HousesForSale WHERE House = ?',(house_id,))
    information = cursor.fetchall()
    
    connection.close()
    
    return information

def get_user_information(id_number):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE ID = ?',(id_number,))
    information = cursor.fetchall()
    
    connection.close()
    
    return information

def edit_user_information(user_id, parameter, new_value):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    if parameter == 'Username':
        cursor.execute('UPDATE users SET Username=? WHERE ID = ?',(new_value,user_id))
        
    if parameter == 'Password':
        cursor.execute('UPDATE users SET Password=? WHERE ID = ?',(new_value,user_id))

    if parameter == 'Email':
        cursor.execute('UPDATE users SET Email=? WHERE ID = ?',(new_value,user_id))
        
    if parameter == 'Bio':
        cursor.execute('UPDATE users SET Bio=? WHERE ID = ?',(new_value,user_id))
    
    connection.commit()
    connection.close()
    
def edit_house_information(house_id, parameter, new_value):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    if parameter == 'Seller':
        cursor.execute('UPDATE HousesForSale SET Seller=? WHERE House = ?',(new_value,house_id))
    if parameter == 'Address':
        cursor.execute('UPDATE HousesForSale SET Address=? WHERE House = ?',(new_value,house_id))
    if parameter == 'Price':
        cursor.execute('UPDATE HousesForSale SET Price=? WHERE House = ?',(new_value,house_id))
    if parameter == 'Size':
        cursor.execute('UPDATE HousesForSale SET Size=? WHERE House = ?',(new_value,house_id))
    if parameter == 'Bedrooms':
        cursor.execute('UPDATE HousesForSale SET Bedrooms=? WHERE House = ?',(new_value,house_id))
    if parameter == 'Bath':
        cursor.execute('UPDATE HousesForSale SET Bath=? WHERE House = ?',(new_value,house_id))
    if parameter == 'Description':
        cursor.execute('UPDATE HousesForSale SET Description=? WHERE House = ?',(new_value,house_id))
    
    connection.commit()
    connection.close()