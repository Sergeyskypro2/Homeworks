from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr" # noqa


def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'company'


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]
    assert row1[0] == 111
    assert row1["name"] == "Барбершоп 'ЦирюльникЪ'"


def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")

    rows = db.execute(sql_statement, company_id = 112).fetchall() # noqa
    assert len(rows) == 1
    assert rows[0]["name"] == "Кодитерская"


def test_select_1_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where \"isActive\" = :isActive and id >= :id") # noqa
    rows = db.execute(sql_statement, id=113, isActive=True).fetchall()

    my_params = {
        "id": 113,
        "isActive": True
    }
    rows = db.execute(sql_statement, my_params).fetchall()
    assert len(rows) == 2


def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into cmpany(\"name\") values (:new_name)")
    db.execute(sql, new_name='Skypro')


def test_update():
    db = create_engine(db_connection_string)
    sql = text("update from company set description = :descr where id = :id")
    db.execute(sql, descr='New descr', id=163)


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    db.execute(sql, id=163)
