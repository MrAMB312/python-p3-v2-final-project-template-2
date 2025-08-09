from models.__init__ import CURSOR, CONN

class Musician:
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Please enter a name.")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Musician instances."""
        sql = """
            CREATE TABLE IF NOT EXISTS musicians (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Musician instances."""
        sql = """
            DROP TABLE IF EXISTS musicians;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name value of the current Musician instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key."""
        sql = """
            INSERT INTO musicians (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """Initialize a new Musician instance and save the object to the database."""
        musician = cls(name)
        musician.save()
        return musician

    def update(self):
        """Update the table row corresponding to the current Musician instance."""
        sql = """
            UPDATE musicians
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Musician instance,
        delete the dictionary entry, and reassign id attribute."""

        sql = """
            DELETE FROM musicians
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Musician object having the attribute values from the table row."""

        musician = cls.all.get(row[0])
        if musician:
            musician.name = row[1]
        else:
            musician = cls(row[1])
            musician.id = row[0]
            cls.all[musician.id] = musician
        return musician

    @classmethod
    def get_all(cls):
        """Return a list containing a Musician object per row in the table."""
        sql = """
            SELECT *
            FROM musicians
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Musician object corresponding to first table row matching specified name."""
        sql = """
            SELECT *
            FROM musicians
            WHERE id is ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def instruments(self):
        """Return list of instruments associated with current musician."""
        from models.instrument import Instrument
        sql = """
            SELECT * FROM instruments
            WHERE musician_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [Instrument.instance_from_db(row) for row in rows]