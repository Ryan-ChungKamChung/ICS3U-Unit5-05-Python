#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program finds volume of a cylinder


def address_format(addressee, street_name, street_number, city_name,
                   province_name, postal_code, apartment = None):

    full_address = addressee

    if apartment != None:
        full_address = (addressee.upper() + '\n' + apartment + "-"
                        + street_number + " " + street_name
                        + '\n' + city_name.upper() + " " +
                        province_name.upper() + "  " + postal_code.upper())
    else:
        full_address = (addressee.upper() + '\n'
                        + street_number + " " + street_name
                        + '\n' + city_name.upper() + " " +
                        province_name.upper() + "  " + postal_code.upper())

        return full_address


def main():
    # Takes user input, passes it to functions and calls them
    
    apartment = None

    print("This tool helps you create a formatted postal address")

    # Input
    addressee = input("Enter Addressee (FIRSTNAME LASTNAME): ")
    
    while True:
        question = input("Do you live in an apartment? (Y/N): ")
        if question.upper() == "Y":
            apartment = input("What is your apartment number? ")
            break
        elif question.upper() == "N":
            break
        else:
            print("Please enter Y or N")

    street_name = input("Enter street name (street type abbreviated, "
                        "abbreviated street direction if needed): ")
    street_number = input("Enter street number: ")

    city_name = input("Enter city: ")
    province_name = input("Enter province (Abbreviated): ")
    postal_code = input("Enter postal code (uppercased, space between the "
                        "first and last 3 characters): ")

    # Calls functions
    if apartment != None:
        address_formatted = address_format(addressee, street_name,
                                           street_number, city_name,
                                           province_name, postal_code,
                                           apartment)
    else:
        address_formatted = address_format(addressee, street_name, 
                                           street_number, city_name,
                                           province_name, postal_code)

    print(address_formatted)

if __name__ == "__main__":
    main()
