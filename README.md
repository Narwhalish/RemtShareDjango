# 1718_RentShare
Repo for Zach G, Maylin and Bryan

## HTML/CSS:
Access website by cloning the repository from GitHub.

**Pages that currently work:** Home, Properties for Sale

**Home:**
Browse through landing page, quick overview.

**Properties for Sale:**
Displays a sample property with sample statistics.

**Viewable pages that are not functional:** Contact, Login

**Contact:**
Displays fake contact information

**Login:**
Displays what our login/create account page will look like

## Python:

Below, the functions that the user can use are enumerated.

### Fake_Database_Creator File

#### create_user_database()

Creates a table of fake users. No input required.

#### create_house_database()

Creates a table of fake houses. No input required.

### querying File

#### login(username, password)

Input username and password, and all user information will be returned.

#### get_all_houses()

Displays ID's of all houses for sale.

#### get_house_information(house_id)

Input a house ID, and receive all information of a single house.

#### get_user_information(id_number)

Input a user ID, and receive all information about a single user.

#### edit_user_information(user_id, parameter, new_value)

Input a user ID, the parameter you wish to change, and the new value in order to change the information on the account. The old value in the given parameter will be replaced with the new one, on the user's account only.

#### edit_house_information(house_id, parameter, new_value)

Input a house ID, the parameter you wish to change, and the new value in order to change the information on the house. The old value in the given parameter will be replaced with the new one, on the given house only.

#### add_new_user(user)
Adds a user to the table of users. A list of all of the values to be entered into the various columns in the database must be entered, in order: Username,First Name,Last Name,Password,Email,Bio,Selling,Invested,Looking,Balance

All parameters above should be Strings, except for Balance, which should be an integer.

The ID of the account will be automatically generated.

#### add_new_house(house)
Adds a house to the table of houses for sale. A list of all of the values to be entered into the various columns in the database must be entered, in order: SellerID,Address,Price,Size,Bedrooms,Bath,Description

The SellerID parameter should be the ID of an already-made user account.

The parameters SellerID, Address, and Description should be Strings. The parameters Price, Size, Bedrooms, and Bath should be integers.

The ID of the account will be automatically generated.
