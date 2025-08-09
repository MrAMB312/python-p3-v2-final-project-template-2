# Phase 3 CLI+ORM Project

# Instrument Database 3000

Welcome to the **Instrument Database 3000**!
This CLI-based application allows users to manage a database of musicians and their instruments.
You can add, update, and delete musicians and their instruments, and view detailed information about each entry.

---

## Setup and Installation

### Prerequisites

- Python 3.x
- SQLite3 (comes pre-installed with most Python distributions)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MrAMB312/python-p3-v2-final-project-template-2
   ```

2. Navigate to the project directory:
   ```bash
   cd python-p3-v2-final-project-template-2
   ```

3. Install the required packages:
   ```bash
   pipenv install
   pipenv shell
   ```

4. Run the application:
   ```bash
   python lib/cli.py
   ```

---

## Usage

Once the application is running, you will see a menu with options to manage musicians and instruments. Here are some controls you can use:

- **Add a musician:** Type 'A' or 'a' to add a new musician.
- **View a musician:** Type the number corresponding to a musician to view their instruments.
- **Add an instrument:** Within a musician's menu, type 'A' or 'a' to add a new instrument.
- **Delete an instrument or musician:** Type 'D' or 'd' in the respective menu.

### Example

Welcome to the Instrument Database 3000!

List of Musicians:

1. John Doe
2. Jane Smith

Please select from the following:
Type 'A' or 'a' to add a new musician.
Type 'E' or 'e' to exit this app.

---

## Project Structure

- **lib/cli.py:** The main script that provides the command-line interface for the application.
- **models/musician.py:** Defines the 'Musician' class ("has-many" class) and its interactions with the database.
- **models/instrument.py:** Defines the 'Instrument' class ("belongs-to" class) and its interactions with the database.
- **lib/helpers.py:** Contains helper functions for database initialization and CRUD operations.

---

## Conclusion

Thank you for using the Instrument Database 3000! Feel free to contribute. Any and all feedback is appreciated.