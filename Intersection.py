def list_intersection(list1, list2):  # Convert lists to sets and find the intersection
    intersection = set(list1) & set(list2) # Convert the result back to a list
    return list(intersection)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = list_intersection(list1, list2)
print("The intersection of the lists is:", result)
