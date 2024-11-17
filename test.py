import database

database_1 = "database_1"
database_2 = "database_2"

# To pass the test, you must change main.py 
# so that Tom is not entered in database_2 and
# JOHN is entered in database_2.
users = database.get_user_table(database_2)

print('\nTesting...')
for user in users:
    print(user)
    if 'Tom' in user[1]:
        print('TEST FAILED')
        break
    elif 'TOM' in user[1]:
        print('TEST FAILED')
        break
    elif 'JOHN' in user[1]:
        print('TEST SUCCEEDED!')
        break
    else:
        continue

