# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            item = input("Enter the item to add: ").strip()
            if item:  # only add non-empty input
                shopping_list.append(item)
                print(f'"{item}" has been added to your shopping list.')
            else:
                print("Item name cannot be empty.")

        elif choice == "2":
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" has been removed from your shopping list.')
            else:
                print(f'"{item}" not found in your shopping list.')

        elif choice == "3":
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
Shopping List Manager
1. Add Item
2. Remove Item
3. View List
4. Exit
Enter your choice (1-4): 1
Enter the item to add: Apples
"Apples" has been added to your shopping list.

Shopping List Manager
1. Add Item
2. Remove Item
3. View List
4. Exit
Enter your choice (1-4): 3

Your Shopping List:
1. Apples

Shopping List Manager
1. Add Item
2. Remove Item
3. View List
4. Exit
Enter your choice (1-4): 2
Enter the item to remove: Oranges
"Oranges" not found in your shopping list.

Shopping List Manager
1. Add Item
2. Remove Item
3. View List
4. Exit
Enter your choice (1-4): 4
Exiting Shopping List Manager. Goodbye!
