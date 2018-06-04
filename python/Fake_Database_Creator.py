import sqlite3
import uuid

def create_connection(database):
    """ Connects to database. Returns connection. Uses current directory. """    
    connection = sqlite3.connect(database)
    return connection

def create_user_database():
    """ 
        Creates table of users with hardcoded information in data.db database 
        Uses Current Working Directory
            
    """
    #Get connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Create Table
    cursor.execute('CREATE TABLE users (ID TEXT PRIMARY KEY, Bio TEXT, Selling TEXT, Invested TEXT, Looking TEXT, Balance INTEGER)')
    #Generate User IDs
    userIds = [str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())]
    #Hardcode User Information
    user1 = [userIds[0], 'I am a pianist from Morganville, New Jersey.','','','',1000000]
    user2 = [userIds[1], 'I am a software engineer from Marlboro, New Jersey.','','','',10000000]
    user3 = [userIds[2], 'I am CEO of Price Waterhouse, currently living in New York City.','','','',100000000]
    user4 = [userIds[3], 'I am the People\'s Champion from Ocean Township, New Jersey.','','','',800000]
    user5 = [userIds[4], 'I am currently developing the world\'s top AI program in Silicon Valley.','','','',550000]
    user6 = [userIds[5], 'I am currently an economics student at Notre Dame university.','','','',750000]
    user7 = [userIds[6], 'I study dance at the Boston Conservatory.','','','',3000000]
    user8 = [userIds[7], 'I am a historian who travels the world, currently living in Xi\'An, China.','','','',4000000]
    user9 = [userIds[8], 'I am currently developing the world\'s most powerful nuclear weapons. My location is secret.','','','',250000]
    user0 = [userIds[9], 'I\'m a comedian living in Las Vegas.','','','',5000000]
    #Create Users
    add_user(user1)
    add_user(user2)
    add_user(user3)
    add_user(user4)
    add_user(user5)
    add_user(user6)
    add_user(user7)
    add_user(user8)
    add_user(user9)
    add_user(user0)
    
    #Save and close connection
    connection.commit()
    connection.close()

def create_house_database():
    """ 
        Creates table of houses with hardcoded information in data.db database 
        Uses Current Working Directory
            
    """
    
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Create Table of HousesForSale
    cursor.execute('CREATE TABLE HousesForSale (House TEXT PRIMARY KEY, Seller TEXT, Address TEXT, Price INTEGER, Size INTEGER, Bedrooms INTEGER, Bath REAL, Description TEXT, Investors TEXT, Invested TEXT, Image TEXT, Images TEXT)')
    
    #Get User ID's
    cursor.execute('SELECT ID FROM users')
    peopleIds = cursor.fetchall()

    #Variables will hold user ID's that will be the sellers of the houses that are hardcoded as fake data
    Maylin = ''
    Bryan = ''
    Zach = ''
    Anna = ''
    Karena = ''
    Sathya = ''
    
    #Generate UUID's for the houses    
    saleHousesIds = [str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4())]    
    #Hardcode house information
    house1 = [saleHousesIds[0], Maylin, '240 Deerfield Rd, Morganville, NJ, 07751', 1000000, 4200, 5, 4.5, 'This is my house.','','','','']
    house2 = [saleHousesIds[1], Zach, '1912 Wilcox Avenue, Monterey Park, CA, 91755', 600000, 3100, 3, 2.5, 'This is my first house in California.','','','','']
    house3 = [saleHousesIds[2], Zach, '1909 Oakgate St, Monterey Park, CA, 91755', 650000, 3100, 3, 3, 'This is my second house in California.','','','','']
    house4 = [saleHousesIds[3], Bryan, '8 Merrill Rd, Marlboro, NJ, 07746', 750000, 3000, 3, 2.5, 'This is a house in Marlboro.','','','','']
    house5 = [saleHousesIds[4], Bryan, '6 Merrill Rd, Marlboro, NJ, 07746', 800000, 3200, 3, 3, 'This is a second house in Marlboro.','','','','']
    house6 = [saleHousesIds[5], Bryan, '4 Merrill Rd, Marlboro, NJ, 07746', 850000, 3400, 4, 3.5, 'This is a third house in Marlboro.','','','','']
    house7 = [saleHousesIds[6], Anna, '2 Vernon Rd, Marlboro, NJ, 07746', 900000, 3600, 4, 4, 'This is Anna\'s old house in Marlboro.','','','','']
    house8 = [saleHousesIds[7], Maylin, '1 Menzel Lane, Holmdel, NJ, 07733', 600000, 2800, 3, 2.5, 'This is my old house.','','','','']
    house9 = [saleHousesIds[8], Karena, '85-44 Homelawn St, Jamaica, NY, 11432', 1250000, 3000, 3, 2.5, 'This is a house in New York.','','','','']
    house0 = [saleHousesIds[9], Sathya, '407 Centerville St, Middleburg, PA, 17842', 500000, 2900, 3, 3, 'This is a house in Pennsylvania.','','','','']
    #Create houses
    add_house(house1)
    add_house(house2)
    add_house(house3)
    add_house(house4)
    add_house(house5)
    add_house(house6)
    add_house(house7)
    add_house(house8)
    add_house(house9)
    add_house(house0)
    
    #Save and close connection
    connection.commit()
    connection.close()

def add_user(user):
    """
        Receives list of information regarding user.
        Inserts given information into database.
        Uses current working directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Add information to database
    cursor.execute("INSERT INTO users (ID, Bio, Selling, Invested, Looking, Balance) VALUES (?,?,?,?,?,?)",(user[0],user[1],user[2],user[3],user[4],\
                    user[5]))
    
    #Save and close connection
    connection.commit()
    connection.close()

def add_house(house):
    """
        Receives list of information regarding house.
        Inserts given information into database.
        Uses current working directory.
    """
    #Get Connection
    connection = create_connection('data.db')
    cursor = connection.cursor()
    
    #Add information to database
    cursor.execute("INSERT INTO HousesForSale (House, Seller, Address, Price, Size, Bedrooms, Bath, Description, Investors, Image, Images) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (house[0], house[1], house[2],\
                    house[3], house[4], house[5], house[6], house[7], house[8], house[9], house[10]))
    
    #Save and close connection
    connection.commit()
    connection.close()