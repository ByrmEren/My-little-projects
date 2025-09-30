
users = tuple()

while True:
    print('Add/Search/Delete/List/Exit')

    search = input('What do you want: ').strip().lower()

    if search == 'add':
        users_list = list(users)

        name = input('Enter your name: ')

        while True:
            phone = input('Enter your phone number: ').strip()
            if phone.isdigit():
                break
            else:
                print('Invalid phone number! Please enter digits only.')

        if any(existing_name.lower() == name.lower() for existing_name, _ in users):
            print(f'{name} is already in the list! Please use another name.')
            continue
        else:
            person = (name, phone)
            users_list.append(person)
            users = tuple(users_list)
            print(f'{person} added to the list.')

    elif search == 'search':
        if len(users) == 0:
            print('List is empty.')
        else:
            find_name = input('Search by name: ')
            found = False

            for name, phone in users:
                if find_name.lower() == name.lower():
                    print(f'User information: {name} - {phone}')
                    found = True
                    break

            if not found:
                print('There is no such person!')

    elif search == 'list':
        if len(users) == 0:
            print('List is empty.')
        else:
            print('\nHere are the users:')
            for i, (name, phone) in enumerate(users, start=1):
                print(f'{i}. {name} - {phone}')
        
    elif search == 'delete':
        if len(users) == 0:
            print('List is empty.')
        else:
            del_name = input('Enter the name to delete: ')
            users_list = list(users)
            found = False

            for i, (name, _) in enumerate(users_list):
                if del_name.lower() == name.lower():
                    removed = users_list.pop(i)
                    users = tuple(users_list)
                    print(f'{removed} has been removed from the list.')
                    found = True
                    break
                
            if not found:
                print('There is no such person!')

    elif search == 'exit':
        print('Goodbye!')
        break
    else:
        print('Invalid enter! try again.')
