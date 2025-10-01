#Joseph DeFilippo period 8 10/1/2025

print("Task 1")
first_and_last_name = input("What is your first and last name?")
space = first_and_last_name.find(" ")
first_name = first_and_last_name[0:space]
last_name = first_and_last_name[space+1:]

print(first_name.title(), last_name.title())
print(first_name[0].lower() + first_name[1:].upper(), last_name[0].lower() + last_name[1:].upper())