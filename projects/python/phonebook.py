#phonebook

import pickle

def menu():
    print('Electronic Phone Book')
    print('=====================')
    print('1. Look up an entry')
    print('2. Add an entry')
    print('3. Delete an entry')
    print('4. List all entries')
    print('5. Save entries')
    print('6. Restore saved entries')
    print('7. Quit')

def pickling():
    myfile = open('phonebook.pickle', 'wb')
    pickle.dump(phonebook, myfile)
    myfile.close()

def depickling():
    global phonebook
    myfile = open('phonebook.pickle', 'rb')
    phonebook = pickle.load(myfile)

def phonebook_funct():
    if selection == 1:
        key = input('Name: ').capitalize()
        print('Phone number: ', phonebook[key])
    elif selection == 2:
        key = input('Name: ').capitalize()
        phone = input('Phone number: ')
        phonebook[key] = phone
        print('Entry stored for {}.'.format(key))
    elif selection == 3:
        key = input('Name: ').capitalize()
        # except KeyError:
        #     print('That entry does not exist.')
        del phonebook[key]
    elif selection == 4:
        for key in phonebook:
            print(key, ':', phonebook[key])
    elif selection == 5:
        pickling()
    elif selection == 6:
        depickling()
    elif selection == 7:
        print('Bye.')

phonebook = {
    'Lora':'123-4567',
    'Bob':'789-0987'
}

menu()
again = 'y'

while again == 'y':
    selection = int(input('What do you want to do? (1-7) '))
    phonebook_funct()
    again = input('Another task? (y/n) ').lower()
else:
    print('Bye.')
