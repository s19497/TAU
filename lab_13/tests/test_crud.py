import sqlite3

import pytest

from src.crud import Crud
from src.my_db import MyDb

con = sqlite3.connect('../database.db')
cur = con.cursor()

crud = Crud(con)
my_db = MyDb(con)


@pytest.fixture(autouse=True)
def run_around():
    my_db.reset_db()
    yield


@pytest.fixture
def student_1():
    params = ['jan@jan.jan', 'jan kowalski', 's19']
    cur.execute("insert into student (email, full_name, indeks) values (?, ?, ?)", params)
    return cur.lastrowid, *params


@pytest.fixture
def student_2():
    params = ['jan2@jan.jan', 'jan kowalski', 's19']
    cur.execute("insert into student (email, full_name, indeks) values (?, ?, ?)", params)
    return cur.lastrowid, *params


def test_create():
    params = ['jan@jan.jan', 'jan kowalski', 's19']
    crud.create(*params)

    user = cur.execute('select * from student').fetchone()
    assert user[1] == params[0]


def test_read(student_1, student_2):
    students = crud.read()
    assert len(students) == 2
    assert students[1][1] == student_2[1]


def test_update(student_1, student_2):
    crud.update(student_1[0], email='email@email.email', full_name='lukasz lukasz')
    updated_student = cur.execute('select * from student where id = ?', (student_1[0],)).fetchone()
    assert updated_student[1] == 'email@email.email'
    assert updated_student[3] == student_1[3]


def test_delete(student_1, student_2):
    crud.delete(student_2[0])
    students = list(cur.execute('select * from student'))
    assert len(students) == 1
    assert students[0][1] == 'jan@jan.jan'
