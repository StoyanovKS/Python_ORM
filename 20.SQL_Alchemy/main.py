from sqlalchemy.orm import sessionmaker
from models import Employee, engine

Session = sessionmaker(bind=engine)
with Session() as session:
    employee = Employee(
        first_name = 'Miroslav',
        last_name='Smith',
        age = 33

    )

    session.add(employee)
    session.commit()

with Session() as session:
    employee = Employee(
        first_name = 'Ivan',
        last_name='SS',
        age = 32

    )

    session.add(employee)
    session.commit()

with Session() as session:
    employee = Employee(
        first_name = 'Petko',
        last_name='BB',
        age = 40

    )

    session.add(employee)
    session.commit()