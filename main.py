import database

database_1 = "database_1"
database_2 = "database_2"

print('Making sure the two databases exist:')
database.create_database(database_1)
database.create_database(database_2)

print('\nRemoving existing data from databases.')
database.delete_users_from_user_table(database_1)
database.delete_users_from_user_table(database_2)

print('\nLets create some users in Database 1:')
database.create_user('Tom', 19, database_1)
database.create_user('Jerry', 25, database_1)
database.create_user('Gerald', 44, database_1)
database.print_database(database_1)

print('\nExtract (E): Storing data read from Database')
all_users_in_1 = database.get_user_table(database_1)

print('Data extracted- this is stored in a Python variable now:')
print(all_users_in_1)

print('\nTransform (T): Transforming the Data')
transformed_users = []
for user in all_users_in_1:
    if (user[1] == 'Tom'):
        continue
    # user[0] we don't need to use this for now
    transformed_users.append((user[1].upper(), user[2] + 10))
    
transformed_users.append(('JOHN', 44))
print('Now that we have transformed the data, lets take a look:')
print(transformed_users)

print('\nLoad (L): Uploading transformed data to new Database')
for user in transformed_users:
    database.create_user(user[0], user[1], database_2)
print(f'Printing contents of {database_2}')
print(database.get_user_table(database_2))

print('\nCongratulations! You have performed ETL between two databases.')