"""Collection of DB entities for the Talks Feedback microservice."""

from sqlalchemy import Boolean, String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Talk(Base):
    """Talk model representation."""

    __tablename__ = 'talks'

    id = Column(Integer(), autoincrement=True, primary_key=True)

    name = Column(String(100), nullable=False)
    positive_votes = Column(Integer(), nullable=False, default=0)
    negative_votes = Column(Integer(), nullable=False, default=0)
    neutral_votes = Column(Integer(), nullable=False, default=0)


TalkTbl = Talk.__table__
