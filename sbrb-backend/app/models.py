from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Role(Base):
    __tablename__ = "role"
    role_name = Column("rname", String(20), primary_key=True)
    role_desc = Column("description", Text)
    skills = relationship("Skill", secondary="role_skill", back_populates="roles", cascade="all, delete")
    staff = relationship("Staff", back_populates="role", cascade="all, delete")
class Skill(Base):
    __tablename__ = "skill"
    skill_name = Column("sname", String(50), primary_key=True)
    skill_desc = Column("description", Text)
    roles = relationship("Role", secondary='role_skill', back_populates="skills", cascade="all, delete")

class RoleSkill(Base):
    __tablename__ = "role_skill"
    role_name = Column('role_name', String(20), ForeignKey('role.rname', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    skill_name = Column('skill_name', String(50), ForeignKey('skill.sname',ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)

class AccessControl(Base):
    __tablename__ = "access_control"
    access_id = Column("ac_id", Integer, primary_key=True)
    access_control_name=  Column("ac_name", String(20))
    staff = relationship("Staff", back_populates="access_control")

class Staff(Base):
    __tablename__ = "staff"
    staff_id = Column("staff_id", Integer, primary_key=True)
    staff_fname = Column("staff_fname", String(50), nullable=False)
    staff_lname = Column("staff_lname", String(50), nullable=False)
    dept = Column("dept", String(50), nullable=False)
    country = Column("country", String(50), nullable=False)
    email = Column("email", String(50), nullable=False)

    role_name = Column("rname", ForeignKey("role.rname"), nullable=False)
    role = relationship("Role", back_populates="staff")

    access_id = Column("ac_id", Integer, ForeignKey("access_control.ac_id"), nullable=False)
    access_control = relationship("AccessControl", back_populates="staff")