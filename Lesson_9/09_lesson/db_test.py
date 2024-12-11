from Data import Data
db = Data("postgresql://postgres:123@localhost:5432/QA")


def test_insert_subject():
    max_id_before = db.get_max_id()
    subject_title = "zavod"
    subject_id = max_id_before + 1
    db.create(subject_title, subject_id)
    max_id_after = db.get_max_id()

    assert max_id_after == subject_id
    db.delete(max_id_after)


def test_update_subject():
    max_id_before = db.get_max_id()
    subject_title = "zavod"
    subject_id = max_id_before + 1
    db.update(subject_title, subject_id)
    new_subject_title = "www"
    max_id_after = db.get_max_id()

    assert new_subject_title != subject_title
    assert max_id_after == subject_id
    db.delete(max_id_after)


def test_detele_subject():
    max_id_before = db.get_max_id()
    subject_title = "zavod"
    subject_id = max_id_before + 1

    db.delete(subject_id)
    max_id_after = db.get_max_id()

    assert max_id_after == max_id_before
    assert subject_title == 0
