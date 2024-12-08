from sqlalchemy import create_engine
from sqlalchemy.sql import text # noqa


class Data:
    __scripts = {
        "insert into": text("INSERT INTO subject(\"subject_title\", \"subject_id\") VALUES (:subject_title, subject_id"), # noqa
        "delete by id": text("DELETE FROM subject WHERE subject_id = :id_to_delete"), # noqa
        "get max id": "select MAX(subject_id) from subject"
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, subject_title, subject_id):
        self.__db.execute(self.__scripts("insert into"), subject_title=subject_title, subject_id=subject_id) # noqa

    def delete(self, id):
        self.__db.execute(self.__scripts("delete by id"), id_to_delete=id)

    def get_max_id(self):
        return self.__db.execute(self.__scripts("get max id")).fetchall()[0][0]
