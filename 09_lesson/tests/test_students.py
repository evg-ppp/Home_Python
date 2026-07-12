from src.models import Student


def test_create_student(db_session):
    student = Student(
        name="Иван",
        email="ivan@test.com"
    )

    db_session.add(student)
    db_session.commit()

    result = db_session.query(Student).filter_by(
        email="ivan@test.com"
    ).first()

    assert result.name == "Иван"

    db_session.delete(student)
    db_session.commit()


def test_update_student(db_session):
    student = Student(
        name="Петр",
        email="petr@test.com"
    )

    db_session.add(student)
    db_session.commit()

    student.name = "Петр Иванов"

    db_session.commit()

    result = db_session.query(Student).filter_by(
        email="petr@test.com"
    ).first()

    assert result.name == "Петр Иванов"

    db_session.delete(student)
    db_session.commit()


def test_delete_student(db_session):
    student = Student(
        name="Удаляемый",
        email="delete@test.com"
    )

    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    result = db_session.query(Student).filter_by(
        email="delete@test.com"
    ).first()

    assert result is None
