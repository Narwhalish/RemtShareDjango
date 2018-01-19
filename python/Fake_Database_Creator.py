import sqlite3

def create_connection(database):
    connection = sqlite3.connect(database)
    return connection

def create_house_database():
    connection = create_connection('houses.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE houses (House INTEGER, Seller TEXT, Location TEXT, Price INTEGER, Size INTEGER)')
    house1 = ['1', 'Maylin', 'Morgan', '5000', '110']
    house2 = ['2', 'Bryan', 'Marlboro', '6000', '120']
    house3 = ['3', 'Zach', 'Holmdel', '7000', '130']
    house4 = ['4', 'Maylin', 'Morgan', '5000', '110']
    add_house(house1)
    add_house(house2)
    add_house(house3)
    add_house(house4)
    
    connection.commit()
    connection.close()

def create_user_database():
    user1 = ['1', 'Maylin', 'Myanmar', 'mahorchler@ctemc.org', '1,2']
    user2 = ['2', 'Bryan', 'Georgia', 'bryao@ctemc.org', '2,3']
    user3 = ['3', 'Zach', 'United States', 'zaglasser@ctemc.org', '1,2,3']
    add_user(user1)
    add_user(user2)
    add_user(user3)

def add_house(house):
    connection = create_connection('houses.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO houses ({ID},{seller},{location},{price},{size}) VALUES (House, Seller, Location, Price, Size)".\
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