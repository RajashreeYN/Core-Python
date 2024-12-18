customers = {     #Creating Dictionary
    1: "Mahi",
    2: "Virat",
    3: "Ruturaj",
    4: "Ishan",
    5: "Jadeja"
}       
print("Customer IDs and Names:") #Displaying Dictionary
for customer_id, name in customers.items():
    print(f"{customer_id}: {name}")
customers[6] = "Pathirana"  #Adding new Customer
print("\nAfter adding Pathirana:")
print(customers)
customers[4] = "Tushar"   #Updating name
print("\nAfter updating Ishan's name to Tushar:")
print(customers)
del customers[2] # Removing Customer
print("\nAfter removing Virat")
print(customers)
customer_id_to_check = 5      #Checking I'd
if customer_id_to_check in customers:
    print(f"\nCustomer ID {customer_id_to_check} is associated with {customers[customer_id_to_check]}")
else:
    print(f"\nCustomer ID {customer_id_to_check} is not in the list")
print("\nAll customer IDs:")  #displaying all id
for customer_id in customers.keys():
    print(customer_id)
print("\nAll customer names:") #Displaying all customer names
for name in customers.values():
    print(name)
