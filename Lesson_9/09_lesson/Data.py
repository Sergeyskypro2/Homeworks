from sqlalchemy import create_engine, text


class Data:
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create(self, subject_title, subject_id):
        with self.__db.begin() as conn:
            conn.execute(text("INSERT INTO subject(\"subject_title\", \"subject_id\") VALUES (:subject_title, :subject_id)"), # noqa
                         {"subject_title": subject_title, "subject_id": subject_id} # noqa
                         )

    def update(self, subject_title, subject_id):
        with self.__db.begin() as conn:
            conn.execute(text("UPDATE subject SET subject_title = :update_title WHERE subject_id = :id_to_update"), # noqa
                         {"update_title": subject_title, "id_to_update": subject_id} # noqa
                         )

    def delete(self, id):
        with self.__db.begin() as conn:
            conn.execute(text("DELETE FROM subject WHERE subject_id = :id_to_delete"), # noqa
                         {"id_to_delete": id}
                         )

    def get_max_id(self):
        with self.__db.begin() as conn:
            result = conn.execute(text("SELECT MAX(subject_id) FROM subject"))
            return result.scalar()
