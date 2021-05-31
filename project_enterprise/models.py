from re import I
from sqlalchemy import Column, Integer, VARCHAR, SMALLINT, DATETIME, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Boolean, Enum
import enum

Base = declarative_base()

class Database(Base):
    __tablename__ = 'database'
    id = Column('db_id', Integer, primary_key=True)
    name = Column('db_name', VARCHAR(50))

class Job(Base):
    __tablename__ = 'job'
    id = Column('job_id', Integer, primary_key=True)
    name = Column('job_name', VARCHAR(100))

class Certification(Base):
    __tablename__ = 'certification'
    id = Column('cert_id', Integer, primary_key=True)
    name = Column('cert_name', VARCHAR(50))

class LookingJob(Base):
    __tablename__ = 'looking_job'
    id = Column('look_id', Integer, primary_key=True)
    job = Column('look_job', VARCHAR(100))

class Task(Base):
    __tablename__ = 'task'
    id = Column('tas_id', Integer, primary_key=True)
    name = Column('tas_name', VARCHAR(50))

class CarreerPlan(Base):
    __tablename__ = 'carreer_plan'
    id = Column('cap_id', Integer, primary_key=True)
    plan = Column('cap_plan', VARCHAR(50))

class EmploymentSector(Base):
    __tablename__ = 'employment_sector'
    id = Column('sec_id', Integer, primary_key=True)
    name = Column('sec_name', VARCHAR(50))

class Country(Base):
    __tablename__ = 'country'
    id = Column('ctr_id', Integer, primary_key=True)
    name = Column('ctr_name', VARCHAR(42))

class Sondage(Base):
    __tablename__ = 'sondage'
    id = Column('sdg_id', Integer, primary_key=True)
    year = Column('sdg_year', SMALLINT)

class EmploymentStatus(Base):
    __tablename__ = 'employment_status'
    id = Column('emp_id', Integer, primary_key=True)
    status = Column('emp_status', VARCHAR(75))

class Education(Base):
    __tablename__ = 'education'
    id = Column('edu_id', Integer, primary_key=True)
    title = Column('edu_title', VARCHAR(50))

class Gender(enum.Enum):
    male = "Male"
    female = "Female"
    other = "Non-binary/third gender"
    na = "Prefer not to say"

class HowManyCompanies(Base):
    __tablename__ = 'how_many_companies'
    id = Column('mcp_id', Integer, primary_key=True)
    many_companies = Column('mcp_many_companies', VARCHAR(75))

class LargestCity(Base):
    __tablename__ = 'largest_city'
    id = Column('pop_id', Integer, primary_key=True)
    name = Column('pop_name', VARCHAR(50))

class OtherDuties(Base):
    __tablename__ = 'other_duties'
    job_id = Column('job_id', Integer, ForeignKey('job.job_id'), primary_key=True)
    sgi_id = Column('sgi_id', Integer, ForeignKey('sondage_item.sgi_id'), primary_key=True)

class TaskPerformed(Base):
    __tablename__ = 'task_performed'
    tas_id = Column('tas_id', Integer, ForeignKey('task.tas_id'), primary_key=True)
    sgi_id = Column('sgi_id', Integer, ForeignKey('sondage_item.sgi_id'), primary_key=True)

class OtherDatabase(Base):
    __tablename__ = 'other_database'
    db_id = Column('db_id', Integer, ForeignKey('database.db_id'), primary_key=True)
    sgi_id = Column('sgi_id', Integer, ForeignKey('sondage_item.sgi_id'), primary_key=True)

class SondageItem(Base):
    __tablename__ = 'sondage_item'
    id = Column('sgi_id', Integer, primary_key=True)
    timestamp = Column('timestamp', DATETIME)
    salary_usd = Column('salary_usd', DECIMAL(10,2))
    postal_code = Column('postal_code', VARCHAR(10))
    years_with_db = Column('years_with_db', SMALLINT)
    manage_staff = Column('manage_staff', Boolean)
    years_with_job = Column('years_with_job', SMALLINT)
    other_people = Column('other_people', Integer)
    company_employee = Column('company_employee', Integer)
    database_servers = Column('database_servers', Integer)
    education_computer = Column('eduction_computer', Boolean)
    hours_worked = Column('hours_worked', Integer)
    telecommute = Column('telecommute', Integer)
    newest_version = Column('newest_version', VARCHAR(50))
    oldest_version = Column('oldest_version', VARCHAR(50))
    gender = Column('gender', Enum(Gender))
    sdg_id = Column(Integer, ForeignKey('sondage.sdg_id'))
    ctr_id = Column(Integer, ForeignKey('country.ctr_id'))
    primary_db_id = Column(Integer, ForeignKey('database.db_id'))
    emp_id = Column(Integer, ForeignKey('employment_status.emp_id'))
    job_id = Column(Integer, ForeignKey('job.job_id'))
    mcp_id = Column(Integer, ForeignKey('how_many_companies.mcp_id'))
    edu_id = Column(Integer, ForeignKey('education.edu_id'))
    cert_id = Column(Integer, ForeignKey('certification.cert_id'))
    pop_id = Column(Integer, ForeignKey('largest_city.pop_id'))
    sec_id = Column(Integer, ForeignKey('employment_sector.sec_id'))
    look_id = Column(Integer, ForeignKey('looking_job.look_id'))
    cap_id = Column(Integer, ForeignKey('carreer_plan.cap_id'))
    sondage = relationship("Sondage", back_populates="sondages")
    other_db = relationship("OtherDatabase", secondary=OtherDatabase)
    other_jobs = relationship("Job", secondary=OtherDuties)
    task_perfomed = relationship("Task", secondary=TaskPerformed)
    country = relationship("Country")
    primary_db = relationship("Database", foreign_keys=[primary_db_id])
    employment_status = relationship("EmploymentStatus")
    job = relationship("Job")
    how_many_companies = relationship("HowManyCompanies")
    education = relationship("Education")
    certification = relationship("Certification")
    largest_city = relationship("LargestCity")
    employment_sector = relationship("EmploymentSector")
    looking_job = relationship("LookingJob")
    carreer_plan = relationship("CarreerPlan")
    

db = create_engine('mysql://akuma06:sdfsdf23@localhost/')
db.execute("DROP DATABASE IF EXISTS simplon;CREATE DATABASE simplon;USE simplon;")
Base.metadata.create_all(db)