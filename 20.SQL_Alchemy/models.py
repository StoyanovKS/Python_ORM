# firstly we have to create a virtual environment
# afterwards we have to install sqlaclhemy and psycopg2


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'migrations_lab4',
#         'USER': 'postgres',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }
from sqlalchemy import String, create_engine, Column, Integer
from sqlalchemy.orm import declarative_base
#CONNECTION_STRING ='<dialect>+<drive>://<username>:<password>@<host>:<port>/database'


#connection string or we can name it DATABASE_URL
engine = create_engine 
from sqlalchemy.orm import declarative_base
#CONNECTION_STRING ='<dialect>+<drive>://<username>:<password>@<host>:<port>/database'
CONNECTION_STRING='postgresql+psycopg2://postgres:admin@localhost:5432/sqlalchemy'


engine = create_engine(CONNECTION_STRING)


Base = declarative_base()


#first model creation

class Employee(Base):
    __tablename__ = 'Employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)
    



# from sqlalchemy.orm import declarative_base, relationship
# from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
# from decouple import config

# DATABASE_URL = config('DATABASE_URL')
# engine = create_engine(DATABASE_URL)

# Base = declarative_base()


# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     email = Column(String)


# class Order(Base):
#     __tablename__ = 'orders'

#     id = Column(Integer, primary_key=True)
#     is_completed = Column(Boolean, default=False)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship('User')


# # Create tables in the database (no migrations management)
# # Base.metadata.create_all(engine)