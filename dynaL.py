def create_dynamic_list():
    my_list = []    # Get 5 elements from the user
    for i in range(5):
        element = input(f"Enter element {i+1}: ")
        my_list.append(element)
    while True:
        print("\nChoose an operation:")
        print("1. Insert a new element")
        print("2. Delete an element")
        print("3. Display the list")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            new_element = input("Enter the new element: ")
            index = int(input("Enter the index to insert at: "))
            my_list.insert(index, new_element)
            print("Element inserted successfully!")

        elif choice == '2':
            element_to_delete = input("Enter the element to delete: ")
            if element_to_delete in my_list:
                my_list.remove(element_to_delete)
                print("Element deleted successfully!")
            else:
                print("Element not found in the list.")

        elif choice == '3':
            print("Current list:", my_list)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_dynamic_list()
