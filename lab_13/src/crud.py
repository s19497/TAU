from sqlite3 import Cursor, Connection


class Crud:
    def __init__(self, connection):
        self.connection: Connection = connection
        self.cursor: Cursor = connection.cursor()

    def create(self, email, full_name, indeks):
        self.cursor.execute(
            'insert into student (email, full_name, indeks) values (?, ?, ?)',
            (email, full_name, indeks)
        )
        self.connection.commit()
        return self.cursor.lastrowid, email, full_name, indeks

    def read(self):
        return list(self.cursor.execute('select * from student'))

    def update(self, oid, **kwargs):
        if not len(kwargs):
            return
        set_keys = ', '.join(f'{i} = ?' for i in kwargs.keys())
        self.cursor.execute(
            f'update student set {set_keys} where id = ?',
            (*kwargs.values(), oid)
        )

    def delete(self, oid):
        self.cursor.execute('delete from student where id = ?', (oid,))
