# lib/helpers.py
from models.musician import Musician
from models.instrument import Instrument


def exit_program():
    print("Thank you for using the Instrument Database 3000. Goodbye!")
    exit()

def initialize_database():
    Musician.create_table()
    Instrument.create_table()


# musician functions
def list_musicians():
    musicians = Musician.get_all()
    if musicians:
        print("List of Musicians:")
        for i, musician in enumerate(musicians, start=1):
            print(f'{i}. {musician.name}')
    else:
        print("***No musicians found. Add a new musician.***")
    return musicians

def create_musician():
    name = input("Enter the musician's name: ")
    try:
        musician = Musician.create(name)
        print(f'Success: {musician}')
    except Exception as exc:
        print("Error creating musician: ", exc)

def delete_musician(musician_id):
    if musician := Musician.find_by_id(musician_id):
        musician.delete()
        print(f'{musician.name} has been deleted from list of musicians.')
    else:
        print("Musician not found. Please try a different number.")
    

# instrument functions
def list_instruments(musician):
    instruments = musician.instruments()
    if instruments:
        print(f"{musician.name}'s instrument list:")
        for i, instrument in enumerate(instruments, start=1):
            print(f'{i}. {instrument.instrument_type}')
    else:
        print(f'No instruments found. Add a new instrument for {musician.name}.')
    return instruments

def create_instrument(musician_id):
    year_manufactured = input("Enter the instrument's year of manufacture (leave blank if unsure): ")
    year_manufactured = int(year_manufactured) if year_manufactured else None

    brand = input("Enter the instrument brand (ex. Stradivarius): ")
    model = input("Enter the instrument model (ex. Servais): ")
    instrument_type = input("Enter the type of instrument (ex. cello): ")

    year_purchased = input("Enter the instrument's year of purchase (leave blank if unsure): ")
    year_purchased = int(year_purchased) if year_purchased else None

    try:
        instrument = Instrument.create(year_manufactured, brand, model, instrument_type, year_purchased, musician_id)
        print(f'Success: {instrument_type}')
    except Exception as exc:
        print("Error creating instrument: ", exc)
    
def delete_instrument(instrument_id):
    if instrument := Instrument.find_by_id(instrument_id):
        instrument.delete()
        print(f'{instrument.instrument_type} has been deleted from list of instruments.')
    else:
        print("Instrument not found. Please try a different number.")


# instrument details functions
def list_instrument_details(instrument):
    print(f"{instrument.instrument_type} details:")
    print(f"Year Manufactured: {instrument.year_manufactured}")
    print(f"Instrument Brand: {instrument.brand}")
    print(f"Instrument Model: {instrument.model}")
    print(f"Year Purchased: {instrument.year_purchased}")

def update_instrument_details(instrument_id):
    if instrument := Instrument.find_by_id(instrument_id):
        try:
            year_manufactured = input("Enter the instrument's new year of manufacture (leave blank if no change or unknown): ")
            if year_manufactured == "":
                year_manufactured = instrument.year_manufactured
            else:
                year_manufactured = int(year_manufactured)
            instrument.year_manufactured = year_manufactured

            brand = input("Enter the instrument's new brand (leave blank if no change): ")
            if brand == "":
                brand = instrument.brand
            instrument.brand = brand

            model = input("Enter the instrument's new model (leave blank if no change): ")
            if model == "":
                model = instrument.model
            instrument.model = model

            year_purchased = input("Enter the instrument's new year of purchase (leave blank if no change or unknown): ")
            if year_purchased == "":
                year_purchased = instrument.year_purchased
            else:
                year_purchased = int(year_purchased)
            instrument.year_purchased = year_purchased

            instrument.update()
            print(f'Success: {instrument.instrument_type} updated')
        except Exception as exc:
            print("Error updating instrument: ", exc)
    else:
        print("Instrument not found.")