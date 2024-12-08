from sqlalchemy import create_engine
from sqlalchemy.sql import text
from Data import Data

db_connection_string = "postgresql://postgres:123@localhost:5432/QA"
db = Data("postgresql://postgres:123@localhost:5432/QA")


def test_insert_subject():
    name = "zavod"
    db.create(name)
    max_id = db.get_max_id()

    db.delete(max_id)

    db = create_engine(db_connection_string)
    sql = text("INSERT INTO subject(\"subject_title\", \"subject_id\") VALUES (:subject_title, subject_id)") # noqa
    db.execute(sql, subject_title="zavod", subject_id=16)


# def test_update():
#     db = create_engine(db_connection_string)
#     sql = text("UPDATE subject SET subject_title = :where subject_id = :subject_title") # noqa
#     db.execute(sql, subject_id=16, subject_title="www")


# def test_delete():
#     subject_title = "zavod"
#     subject_id = "16"
#     db.create(subject_title, subject_id)
#     max_id = db.get_max_id()

#     deleted = db.delete(max_id)
#     assert deleted["id"] == max_id

#     db = create_engine(db_connection_string)
#     sql = text("DELETE FROM subject WHERE subject_id = 16")
#     db.execute(sql, id=16)
