"""Collection of DB entities for the Talks Feedback microservice."""

from sqlalchemy import Boolean, String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
matadata = Base.metadata


class Talk(Base):
    """Talk model representation."""

    __tablename__ = 'talks'

    id = Column(Integer(), autoincrement=True, primary_key=True)

    name = Column(String(100), nullable=False)
    votes = Column(Integer(), nullable=False, default=False)
