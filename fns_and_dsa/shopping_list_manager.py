def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # start with an empty list
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"✅ '{item}' has been added to your shopping list.")
        
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"❌ '{item}' has been removed from your shopping list.")
            else:
                print(f"⚠️ '{item}' not found in the list.")
        
        elif choice == '3':
            if shopping_list:  # check if list is not empty
                print("\n🛒 Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
            print("👋 Goodbye! Happy shopping.")
            break  # exit the loop
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
