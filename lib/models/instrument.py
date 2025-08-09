from models.__init__ import CURSOR, CONN
from models.musician import Musician

class Instrument:
    all = {}

    def __init__(self, year_manufactured, brand, model, instrument_type, year_purchased, musician_id, id=None):
        self.id = id
        self.year_manufactured = year_manufactured
        self.brand = brand
        self.model = model
        self.instrument_type = instrument_type
        self.year_purchased = year_purchased
        self.musician_id = musician_id

    @property
    def year_manufactured(self):
        return self._year_manufactured

    @year_manufactured.setter
    def year_manufactured(self, year_manufactured):
        if year_manufactured is None:
            self._year_manufactured = None
        elif isinstance(year_manufactured, int) and 1000 <= year_manufactured <= 9999:
            self._year_manufactured = year_manufactured
        else:
            raise ValueError("Please enter a four-digit year of manufacture or leave blank.")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and len(brand):
            self._brand = brand
        else:
            raise ValueError("Please enter the instrument brand.")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and len(model):
            self._model = model
        else:
            raise ValueError("Please enter the instrument model.")

    @property
    def instrument_type(self):
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        if isinstance(instrument_type, str) and len(instrument_type):
            self._instrument_type = instrument_type
        else:
            raise ValueError("Please enter the instrument type.")

    @property
    def year_purchased(self):
        return self._year_purchased

    @year_purchased.setter
    def year_purchased(self, year_purchased):
        if year_purchased is None:
            self._year_purchased = None
        elif isinstance(year_purchased, int) and 1000 <= year_purchased <= 9999:
            self._year_purchased = year_purchased
        else:
            raise ValueError("Please enter a four-digit year of purchase or leave blank.")

    @property
    def musician_id(self):
        return self._musician_id

    @musician_id.setter
    def musician_id(self, musician_id):
        if type(musician_id) is int and Musician.find_by_id(musician_id):
            self._musician_id = musician_id
        else:
            raise ValueError("musician_id must reference a musician in the database.")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Instrument instances."""
        sql = """
            CREATE TABLE IF NOT EXISTS instruments (
            id INTEGER PRIMARY KEY,
            year_manufactured INTEGER,
            brand TEXT,
            model TEXT,
            instrument_type TEXT,
            year_purchased INTEGER,
            musician_id INTEGER,
            FOREIGN KEY (musician_id) REFERENCES musicians(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Instrument instances."""
        sql = """
            DROP TABLE IF EXISTS instruments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the year manufactured, brand, model, instrument type, year purchased, and musician id values of the current Instrument object.
        Update object id attribute using the primary key value of new row.
        Save the object in the local dictionary using the table row's PK as dictionary key."""
        sql = """
            INSERT INTO instruments (year_manufactured, brand, model, instrument_type, year_purchased, musician_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.year_manufactured, self.brand, self.model, self.instrument_type, self.year_purchased, self.musician_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Instrument instance."""
        sql = """
            UPDATE instruments
            SET year_manufactured = ?, brand = ?, model = ?, instrument_type = ?, year_purchased = ?, musician_id = ?
            WHERE id = ?
            """

        CURSOR.execute(sql, (self.year_manufactured, self.brand, self.model,
                             self.instrument_type, self.year_purchased, self.musician_id,
                             self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Instrument instance,
        delete the dictionary entry, and reassign id attribute."""

        sql = """
            DELETE FROM instruments
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, year_manufactured, brand, model, instrument_type, year_purchased, musician_id):
        """Initialize a new Instrument instance and save the object to the database."""
        instrument = cls(year_manufactured, brand, model, instrument_type, year_purchased, musician_id)
        instrument.save()
        return instrument

    @classmethod
    def instance_from_db(cls, row):
        """Return an Instrument object having the attribute values from the table row."""
        instrument = cls.all.get(row[0])
        if instrument:
            instrument.year_manufactured = row[1]
            instrument.brand = row[2]
            instrument.model = row[3]
            instrument.instrument_type = row[4]
            instrument.year_purchased = row[5]
            instrument.musician_id = row[6]
        else:
            instrument = cls(row[1], row[2], row[3], row[4], row[5], row[6])
            instrument.id = row[0]
            cls.all[instrument.id] = instrument
        return instrument

    @classmethod
    def get_all(cls):
        """Return a list containing one Instrument object per table row."""
        sql = """
            SELECT *
            FROM instruments
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Instrument object corresponding to the table row matching the specified primary key."""
        sql = """
            SELECT *
            FROM instruments
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None