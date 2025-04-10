from sqlalchemy.orm import sessionmaker
from models import Employee, engine

# Session = sessionmaker(bind=engine)
# with Session() as session:
#     employees = session.query(Employee).all()
#     for employee in employees:
#         print(employee.first_name, employee.last_name, employee.age)


# Session = sessionmaker(bind=engine)
# with Session() as session:
#     employees = session.query(Employee).filter(Employee.age>=40)
#     for employee in employees:
#         print(employee.first_name, employee.last_name, employee.age)


Session = sessionmaker(bind=engine)
with Session() as session:
    employees = session.query(Employee).where(Employee.first_name.startswith('I'))
    for employee in employees:
        print(employee.first_name, employee.last_name, employee.age)