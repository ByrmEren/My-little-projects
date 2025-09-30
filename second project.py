shopping = ()
print(shopping)
while True:
    print('\n1 - Add product')
    print('2 - Delete product')
    print('3 - Look list')
    print('4 - Sort list')
    print('5 - Count product')
    print('6 - Search product')
    print('7 - Clear the list')
    print('8 - Exit')
    user = input('What do you want: ')
    
    if user == '1':
        shopping_list = list(shopping)
        product = input('Enter product: ')
        shopping_list.append(product)
        shopping = tuple(shopping_list)
        print(f'{product} added the list!')

    elif user == '2':
        if not shopping:
            print('List is empty!')
        else:
            print(f'Current list: {shopping}')
           
            product = input('Enter product to delete: ')
            shopping_list = list(shopping)
            
            if product in shopping_list:
                shopping_list.remove(product)
                shopping = tuple(shopping_list)
                print(f'{product} deleted from the list!')
            else:
                print(f'{product} is not in the list!')

    elif user == '3':
        if not shopping:
            print('List is empty!')
        else:
            print('\nShopping list:')
            for i, item in enumerate(shopping, start=1):
                print(f'{i}. {item}')

    elif user == '4':
        shopping_list = list(shopping)
        shopping_list.sort()
        shopping = tuple(shopping_list)
        print('List is sorted!')

    elif user == '5':
        shopping_list = list(shopping)
        product_count = len(shopping_list)
        print(f'Shopping product count: {product_count}')
        shopping = tuple(shopping_list)

    elif user == '6':
        search_product = input('Search product: ')
        if search_product in shopping:
            print(f'{search_product} is in the list!')
        else:
            print(f'{search_product} not in the list!')
    
    elif user == '7':
        shopping_list = list(shopping)
        shopping_list.clear()
        shopping = tuple(shopping_list)
        print(f'{shopping} shopping list now cleared!')

    elif user == '8':
        print('Program ended. See you!')
        break
    else:
        print('Invalid Enter! Please enter a number between 1 and 8')
        continue
