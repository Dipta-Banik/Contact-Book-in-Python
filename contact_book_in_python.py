# -*- coding: utf-8 -*-
"""Contact Book in Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lpCq_gLOFSTHUQHjqMooEgdWC2KvGyLQ
"""

def is_valid_phone_number(phone):
    return phone.isdigit()

def is_unique_name(name):
    return name not in names

def is_unique_phone_number(phone):
    return phone not in phone_numbers

def detect_country_code(country_name):
    country_name = country_name.lower()
    country_code = country_code_mapping.get(country_name)
    if country_code:
        return country_code
    else:
        print("Country code for {} is not available. Assuming default country code.".format(country_name))
        return default_country_code

def print_contacts():
    print("\nName\t\t\tPhone Number\n")
    for i in range(len(names)):
        print("{}\t\t\t+{}{}".format(names[i], country_codes[i], phone_numbers[i]))

def search_contact():
    search_term = input("\nEnter search term: ")
    print("Search result:")
    if search_term in names:
        index = names.index(search_term)
        phone_number = phone_numbers[index]
        print("Name: {}, Phone Number: +{}{}".format(search_term, country_codes[index], phone_number))
    else:
        print("Name Not Found")

names = []
phone_numbers = []
country_codes = []

country_code_mapping = {
    "india": "91",
    "usa": "1",
    # Add more country code mappings as needed
}

default_country_code = "91"  # Default country code (India)

while True:
    choice = input("\nWhat would you like to do?\n1. Add a contact\n2. Search for a contact\n3. Show all contacts\n4. Exit\nEnter your choice: ")

    if choice == '1':
        name = input("Name: ")
        phone_number = input("Phone Number: ")

        while not is_valid_phone_number(phone_number):
            print("Invalid phone number. Please enter only digits.")
            phone_number = input("Phone Number: ")

        if not is_unique_name(name):
            print("Name already exists. Please enter a unique name.")
            continue

        if not is_unique_phone_number(phone_number):
            print("Phone number already exists. Please enter a unique phone number.")
            continue

        country_name = input("Country (Optional, press Enter to skip): ")
        country_code = detect_country_code(country_name)

        names.append(name)
        phone_numbers.append(phone_number)
        country_codes.append(country_code)

    elif choice == '2':
        search_contact()

    elif choice == '3':
        print_contacts()

    elif choice == '4':
        break

    else:
        print("Invalid choice. Please enter a valid choice.")

print("Goodbye!")
