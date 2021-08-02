from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name, secret_word):
    user = User(username=name, password_hash=secret_word)
    session.add(user)
    session.commit()

def query_all():
	users = session.query(User).all()
	return users

def get_user(username):
    """Find the first user in the DB, by their username."""
    return session.query(User).filter_by(username=username).first()

def print_all():
	print(session.query(User).all())

for prod in query_all():
    print(prod.username, prod.id)

def remove_all():
	session.query(User).delete()
	session.commit()

# remove_all()

for prod in query_all():
    print(prod.username, prod.id)