from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Numeric, Binary, Boolean, Float
from sqlalchemy import create_engine, UniqueConstraint, func

from config import settings

ENGINE = create_engine(settings.SQL_URI, pool_recycle=3600)

SESSION_MAKER = sessionmaker()
SESSION_MAKER.configure(bind=ENGINE)

BASE = declarative_base()
SESSION = SESSION_MAKER(autocommit=False,
                        autoflush=True,
                        bind=ENGINE)

def add_to_session(objects):
    if type(objects) == list:
        for object in objects:
            SESSION.add(object)
    else:
        SESSION.add(objects)

def commit_session():
    SESSION.commit()

def reset_db():
    session = SESSION_MAKER()
    BASE.metadata.drop_all(ENGINE)
    BASE.metadata.create_all(ENGINE)
    session.close()

class Word(BASE):
    __tablename__ = 'words'

    # Columns
    id = Column(Integer, primary_key=True, nullable=False)
    word_value = Column(String(100), nullable=False)

    @classmethod
    def add_word(cls, word_value):
        new_word = cls(word_value=word_value)
        add_to_session(new_word)
        commit_session()

    @classmethod
    def get_all_words(cls):
        return SESSION.query(cls).all()