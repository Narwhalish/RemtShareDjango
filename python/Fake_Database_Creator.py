import sqlite3
import uuid

def create_connection(database):
    connection = sqlite3.connect(database)
    return connection

def create_house_database():
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE HousesForSale (House TEXT PRIMARY KEY, Seller TEXT, Address TEXT, Price INTEGER, Size INTEGER, Bedrooms INTEGER, Bath INTEGER, Description TEXT, Investors TEXT, Image TEXT, Images TEXT)')
    saleHousesIds = [str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4()),str(uuid.uuid4())]
    house1 = [saleHousesIds[0], 'Maylin', 'Morgan', '5000', '110']
    house2 = [saleHousesIds[1], 'Bryan', 'Marlboro', '6000', '120']
    house3 = [saleHousesIds[2], 'Zach', 'Holmdel', '7000', '130']
    house4 = [saleHousesIds[3], 'Maylin', 'Morgan', '5000', '110']
    house5 = [saleHousesIds[3], 'Maylin', 'Morgan', '5000', '110']
    house6 = [saleHousesIds[3], 'Maylin', 'Morgan', '5000', '110']
    house7 = [saleHousesIds[3], 'Maylin', 'Morgan', '5000', '110']
    house8 = [saleHousesIds[3], 'Maylin', 'Morgan', '5000', '110']
    house9 = [saleHousesIds[3], 'Maylin', 'Morgan', '5000', '110']
    house0 = [saleHousesIds[3], 'Maylin', 'Morgan', '5000', '110']
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
    
    connection.commit()
    connection.close()

def create_user_database():
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE users (ID TEXT PRIMARY KEY, Username TEXT, First TEXT, Last TEXT, Password TEXT, Email TEXT, Bio TEXT, Image TEXT, Selling TEXT, Invested TEXT, Looking TEXT, Balance INTEGER)')
    userIds = [str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())]
    user1 = [userIds[0], 'Maylin', 'Maylin', 'Horchler', '123456', 'mahorchler@ctemc.org', 'I am a pianist from Morganville, New Jersey.', userIds[0] + '.img','','','',1000000]
    user2 = [userIds[1], 'Bryan', 'Bryan', 'Yao', '234567', 'bryao@ctemc.org', 'I am a software engineer from Marlboro, New Jersey.', userIds[1] + '.img','','','',10000000]
    user3 = [userIds[2], 'Zach', 'Zachary', 'Glasser', '345678', 'zaglasser@ctemc.org', 'I am CEO of Price Waterhouse, currently living in New York City.', userIds[2] + '.img','','','',100000000]
    user4 = [userIds[3], 'Daniel', 'Daniel', 'Du', '456789', 'dadu@ctemc.org', 'I am the People\'s Champion from Ocean Township, New Jersey.', userIds[3] + '.img','','','',800000]
    user5 = [userIds[4], 'Sathya', 'Sathya', 'Edamadaka', '567891', 'saedamadaka@ctemc.org', 'I am currently developing the world\'s top AI program in Silicon Valley.', userIds[4] + '.img','','','',550000]
    user6 = [userIds[5], 'Emily', 'Emily', 'Liu', '678912', 'emiliu@ctemc.org', 'I am currently an economics student at Notre Dame university.', userIds[5] + '.img','','','',750000]
    user7 = [userIds[6], 'Karena', 'Karena', 'Yan', '789123', 'kayan@ctemc.org', 'I study dance at the Boston Conservatory.', userIds[6] + '.img','','','',3000000]
    user8 = [userIds[7], 'Anna', 'Anna', 'Cai', '891234', 'ancai@ctemc.org', 'I am a historian who travels the world, currently living in Xi\'An, China.', userIds[7] + '.img','','','',4000000]
    user9 = [userIds[8], 'Steven', 'Steven', 'Liu', '912345', 'stliu@ctemc.org', 'I am currently developing the world\'s most powerful nuclear weapons. My location is secret.', userIds[8] + '.img','','','',250000]
    user0 = [userIds[9], 'Zach', 'Zachary', 'Colucci', '13579', 'zacolucci@ctemc.org', 'I\'m a comedian living in Las Vegas.', userIds[9] + '.img','','','',5000000]
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
    
    connection.commit()
    connection.close()

def add_house(house):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO houses (House,Seller,Location,Price,Size) VALUES (?, ?, ?, ?, ?)", (house[0], house[1], house[2], house[3], house[4]))

    connection.commit()
    connection.close()
    
def add_user(user):
    connection = create_connection('data.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (ID, Username, First, Last, Password, Email, Bio, Image, Selling, Invested, Looking, Balance) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(user[0],user[1],user[2],user[3],user[4]/
                    user[5],user[6],user[7],user[8],user[9],user[10],user[11]))
    
    connection.commit()
    connection.close()