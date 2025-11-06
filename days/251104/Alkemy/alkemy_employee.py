from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Float, create_engine


Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    job_title = Column(String(150), nullable=False)
    salary = Column(Float, nullable=False)

    def __repr__(self):
        return f'[id={self.id}, name={self.name}, job_title={self.job_title}, salary={self.salary}]'
     
# setup the database

engine = create_engine('sqlite:///employees_db.sqlite', echo=True) #create database if not exist
Base.metadata.create_all(engine) # create the table for the model class


# CRUD Operation --> Setup things for the transaction 

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# CRUD 

Virat = Employee(name = 'Virat', job_title = 'King Kholi', salary = 120000 )
# session.add(Virat)

# Millar = Employee(name = 'Millar', job_title = 'Killer Millar', salary = 140000 )
# session.add(Millar)

# Shane = Employee(name = 'Shane', job_title = 'All rounder', salary = 160000 )
# session.add(Shane)


employee = session.query(Employee)
print(employee)

# millar = session.query(Employee).filter_by(name = 'Millar').first()
# print(millar)

# Millar.salary = 180000

session.delete(Virat)
session.commit()