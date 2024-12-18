def reverse_list(my_list):
    reversed_list = my_list[::-1]
    return reversed_list
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(my_list)
    print("Original list:", my_list)
    print("Reversed list:", reversed_list)
