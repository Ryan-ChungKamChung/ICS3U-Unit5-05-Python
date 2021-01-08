#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program outputs a formatted mailing address


def address_format(addressee, street, street_number, city,
                   province, postal_code, apartment=None):
    # Formats the inputs from main()

    # Process
    full_address = addressee
    if apartment is not None:
        full_address = (addressee.upper() + '\n' + apartment + "-"
                        + street_number + " " + street
                        + '\n' + city.upper() + " " +
                        province.upper() + "  " + postal_code.upper())
    else:
        full_address = (addressee.upper() + '\n'
                        + street_number + " " + street
                        + '\n' + city.upper() + " " +
                        province.upper() + "  " + postal_code.upper())

    return full_address


def main():
    # Takes user input, passes it to functions and calls them

    apartment = None

    print("This tool helps you create a formatted postal address")

    # Input
    addressee = input("Enter addressee (FIRSTNAME LASTNAME): ")

    while True:
        question = input("Do you live in an apartment? (Y/N): ")
        if question.upper() == "Y":
            apartment = input("What is your apartment number? ")
            break
        elif question.upper() == "N":
            break
        else:
            print("Please enter Y or N")

    street = input("Enter street name (street type abbreviated): ")
    street_number = input("Enter street number: ")

    city = input("Enter city name: ")
    province = input("Enter province name (Abbreviated): ")
    postal_code = input("Enter postal code (first 3 digits separated from"
                        " the last 3): ")

    # Calls functions
    if apartment is not None:
        address_formatted = address_format(addressee, street,
                                           street_number, city,
                                           province, postal_code,
                                           apartment)
    else:
        address_formatted = address_format(addressee, street,
                                           street_number, city,
                                           province, postal_code)

    # Output
    print(" ")
    print(address_formatted)


if __name__ == "__main__":
    main()
