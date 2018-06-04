import sqlite3
import uuid

def create_connection(database):
    """ Connects to database. Returns connection. Uses current directory. """
    connection = sqlite3.connect(database)
    return connection

def get_all_houses():
    """
        Returns ID's of all houses.
        Uses current directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Fetch ID's of all houses
    cursor.execute('SELECT House FROM HousesForSale')
    information = cursor.fetchall()
    
    #Close connection
    connection.close()
    
    return information

def get_all_users():
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT ID FROM users')
    peopleIds = cursor.fetchall()
    print peopleIds

def get_house_information(house_id):
    """
       Receives the ID of an already-existing house
       Returns all of the information about that house.
       Uses current directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Fetch information about house with given ID
    cursor.execute('SELECT * FROM HousesForSale WHERE House = ?',(house_id,))
    information = cursor.fetchall()
    
    #Close Connection
    connection.close()
    
    return information

def get_user_information(id_number):
    """
       Receives the ID of an already-existing user
       Returns all of the information about that user.
       Uses current directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Fetch information about user with given ID
    cursor.execute('SELECT * FROM users WHERE ID = ?',(id_number,))
    information = cursor.fetchall()
    
    #Close Connection
    connection.close()
    
    return information

def edit_user_information(user_id, parameter, new_value):
    """
       Receives the ID of an already-existing user, the parameter to be changed, and the value to change it to.
       Changes the parameter of that user to the new value.
       Uses current directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Determine which parameter is to be changed, and change it
    if parameter == 'Username':
        cursor.execute('UPDATE users SET Username=? WHERE ID = ?',(new_value,user_id))
        
    if parameter == 'Password':
        cursor.execute('UPDATE users SET Password=? WHERE ID = ?',(new_value,user_id))

    if parameter == 'Email':
        cursor.execute('UPDATE users SET Email=? WHERE ID = ?',(new_value,user_id))
        
    if parameter == 'Bio':
        cursor.execute('UPDATE users SET Bio=? WHERE ID = ?',(new_value,user_id))
    
    #Save and close connection
    connection.commit()
    connection.close()
    
def edit_house_information(house_id, parameter, new_value):
    """
       Receives the ID of an already-existing house, the parameter to be changed, and the value to change it to.
       Changes the parameter of that house to the new value.
       Uses current directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Determine which parameter is to be changed, and change it
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
    
    #Save and close connection
    connection.commit()
    connection.close()

def new_user_investment(user, house):
    """
       Receives the ID of a user and house.
       Changes the houses invested in for that user - adds new house to list
       Uses current directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Get existing houses invested in
    cursor.execute('SELECT Invested FROM users WHERE User = ?',(user))
    information = cursor.fetchall()
    
    #Add the new house to the list of existing houses
    information = information + ',' + house
    cursor.execute('UPDATE users SET Invested = ? WHERE User = ?',(information,user))

def new_house_investment(user, house, amount):
    """
       Receives the ID of a user, house, and amount.
       Changes the invested users for that house - adds user to list of invested users.
       Changes the invested amounts for that house - adds amount to list of invested amounts.
       Uses current directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Get existing investors invested in house
    cursor.execute('SELECT Investors FROM HousesForSale WHERE House = ?',(house))
    investors = cursor.fetchall()
    
    #Add new investor to existing investors
    investors = investors + ',' + user
    cursor.execute('UPDATE HousesForSale SET Investors = ? WHERE House = ?',(investors,house))
    
    #Get existing amounts invested in house
    cursor.execute('SELECT Invested FROM HousesForSale WHERE House = ?',(house))
    invested = cursor.fetchall()
    
    #Add new amount to existing amounts
    invested = invested + ',' + amount
    cursor.execute('UPDATE HousesForSale SET Invested = ? WHERE House = ?',(invested,house))

def remove_user_investment(user, rehouse):
    """
       Receives the ID of a user and house.
       Changes the houses invested in for that user - remove house from list
       Uses current directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Get existing houses invested in
    cursor.execute('SELECT Invested FROM users WHERE User = ?',(user))
    information = cursor.fetchall()
    
    #Delete the house from the list of existing houses
    houses = information.split(',')
    houses.remove(rehouse)
    newInformation = ''
    for house in houses:
        newInformation += house + ','
    cursor.execute('UPDATE users SET Invested = ? WHERE User = ?',(newInformation,user))

def remove_house_investment(reuser, house, reamount):
    """
       Receives the ID of a user, house, and amount.
       Changes the invested users for that house - removes user from list of invested users.
       Changes the invested amounts for that house - removes amount from list of invested amounts.
       Uses current directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Get existing investors invested in house
    cursor.execute('SELECT Investors FROM HousesForSale WHERE House = ?',(house))
    investors = cursor.fetchall()
    
    #Remove investor from existing investors
    investors = investors.split(',')
    investors.remove(reuser)
    newInvestors = ''
    for investor in investors:
        newInvestors += investor + ','
    cursor.execute('UPDATE HousesForSale SET Investors = ? WHERE House = ?',(newInvestors,house))
    
    #Get existing amounts invested in house
    cursor.execute('SELECT Invested FROM HousesForSale WHERE House = ?',(house))
    invested = cursor.fetchall()
    
    #Remove amount from existing amounts
    invested = invested.split(',')
    invested.remove(reamount)
    newInvested = ''
    for invest in invested:
        newInvested += invest + ','
    cursor.execute('UPDATE HousesForSale SET Invested = ? WHERE House = ?',(newInvested,house))

def add_new_user(user):
    """
        Receives list of information regarding a new user.
        Generates new UUID for them.
        Inserts UUID and given information into database.
        Uses current working directory.
    """
    #Generate new UUID
    ID = str(uuid.uuid4())
    
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Insert information into data table
    cursor.execute("INSERT INTO users (ID, Username, First, Last, Password, Email, Bio, Image, Selling, Invested, Looking, Balance) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(ID,user[0],user[1],user[2],user[3],\
                    user[4],user[5],ID + '.img',user[6],user[7],user[8],user[9]))
    
    #Save and close connection
    connection.commit()
    connection.close()

def add_new_house(house):
    """
        Receives list of information regarding a new house.
        Generates new UUID for it.
        Inserts UUID and given information into database.
        Uses current working directory.
    """
    #Generate new UUID
    ID = str(uuid.uuid4())
    
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Insert information into data table
    cursor.execute("INSERT INTO HousesForSale (House, Seller, Address, Price, Size, Bedrooms, Bath, Description, Investors, Image, Images) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(ID,house[0],house[1],house[2],house[3],\
                    house[4],house[5],house[6],'',ID + '.img',''))
    
    #Save and close connection
    connection.commit()
    connection.close()

def delete_user(ID):
    """
        Receives a user ID of an already-existing user.
        Deletes user's information from data table.
        Uses current working directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Delete Information
    cursor.execute("DELETE FROM users WHERE ID=?",(ID,))
    
    #Save and close connection
    connection.commit()
    connection.close()

def delete_house(ID):
    """
        Receives a house ID of an already-existing house.
        Deletes house's information from data table.
        Uses current working directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Delete Information
    cursor.execute("DELETE FROM HousesForSale WHERE House=?",(ID,))
    
    #Save and close connection
    connection.commit()
    connection.close()