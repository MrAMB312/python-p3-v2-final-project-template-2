# lib/cli.py
from models.musician import Musician
from models.instrument import Instrument
from helpers import (
    exit_program,
    initialize_database,
    list_musicians,
    create_musician,
    delete_musician,
    list_instruments,
    create_instrument,
    delete_instrument,
    list_instrument_details,
    update_instrument_details
)

def instrument_menu(instrument):
    while True:
        print("---")
        list_instrument_details(instrument)

        print("---")
        menu3()
        print("---")
        choice = input("> ")

        if choice.lower() == "d":
            print("---")
            delete_instrument(instrument.id)
            return
        elif choice.lower() == "u":
            print("---")
            update_instrument_details(instrument.id)
        elif choice.lower() == "b":
            return
        elif choice.lower() == "e":
            print("---")
            exit_program()
            break
        else:
            print("---")
            print("Invalid choice. Please try again.")
        

def musician_menu(musician):
    while True:
        print("---")
        instruments = list_instruments(musician)

        print("---")
        menu2()
        print("---")
        choice = input("> ")

        if choice.lower() == "a":
            print("---")
            create_instrument(musician.id)
        elif choice.lower() == "d":
            print("---")
            delete_musician(musician.id)
            break
        elif choice.lower() == "m":
            break
        elif choice.lower() == "e":
            print("---")
            exit_program()
            break
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index <= len(instruments):
                instrument_menu(instruments[index])
        else:
            print("Invalid choice. Please try again.")
    

def main():
    initialize_database()
    while True:
        print("---")
        print("Welcome to the Instrument Database 3000!")
        print("---")
        musicians = list_musicians()

        print("---")
        menu1()
        print("---")
        choice = input("> ")

        if choice.lower() == "a":
            print("---")
            create_musician()
            print("---")
        elif choice.lower() == "e":
            print("---")
            exit_program()
            break
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index <= len(musicians):
                musician_menu(musicians[index])
        else:
            print("Invalid choice. Please try again.")


def menu1():
    print("Please select from the following:")
    print("If musicians are listed above, type the numer of a musician to view their instruments.")
    print("Type 'A' or 'a' to add a new musician.")
    print("Type 'E' or 'e' to exit this app.")

def menu2():
    print("Please select from the following:")
    print("If instruments are listed above, type the number of an instrument to view its details.")
    print("Type 'A' or 'a' to add a new instrument.")
    print("Type 'D' or 'd' to delete this musician. Please note, this will also delete all instruments associated with this musician.")
    print("Type 'M' or 'm' to go back to the main menu.")
    print("Type 'E' or 'e' to exit this app.")

def menu3():
    print("Please select from the following:")
    print("Type 'D' or 'd' to delete this instrument.")
    print("Type 'U' or 'u' to update the information for this instrument.")
    print("Type 'B' or 'b' to go back to the previous menu.")
    print("Type 'E' or 'e' to exit this app.")


if __name__ == "__main__":
    main()
