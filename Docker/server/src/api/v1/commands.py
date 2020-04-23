import click
from flask.cli import with_appcontext
from .models import db
from .extensions import guard
from .models.User_model import Users
from .models.Role_model import Roles
from .models.Products_model import Products
import uuid
import datetime

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.drop_all()
    db.create_all()

@click.command(name='create_roles')
@with_appcontext
def create_roles():
    admin = Roles(name='Admin',description='Administrator')
    developer = Roles(name='Developer',description='User Developer')
    seller = Roles(name='Seller',description='User can sell and view')
    viewer = Roles(name='Viewer',description='User only can view')

    db.session.add_all([admin,developer,seller,viewer])
    db.session.commit()

@click.command(name='create_users')
@with_appcontext
def create_users():
    one = Users(public_id=str(uuid.uuid4()),
                first_name='One',
                last_name = 'single',
                password=guard.hash_password('one'),
                email='one@gmail.com',
                birth_date = datetime.date(1992, 4, 13),
                created_date = datetime.datetime.now(),
                role_id = 1,
                ) 
    two = Users(public_id=str(uuid.uuid4()),
                first_name='Two',
                last_name = 'single',
                password=guard.hash_password('two'),
                email='two@gmail.com',
                birth_date = datetime.date(1992, 8, 15),
                created_date = datetime.datetime.now(),
                role_id = 2,
                ) 
    
    three = Users(public_id=str(uuid.uuid4()),
                first_name='Three',
                last_name = 'single',
                password=guard.hash_password('three'),
                email='three@gmail.com',
                birth_date = datetime.date(1998, 1, 22),
                created_date = datetime.datetime.now(),
                role_id = 3,
                ) 

    four = Users(public_id=str(uuid.uuid4()),
                first_name='Four',
                last_name = 'single',
                password=guard.hash_password('four'),
                email='four@gmail.com',
                birth_date = datetime.date(1993, 9, 19),
                created_date = datetime.datetime.now(),
                ) 
    db.session.add_all([one,two,three,four])
    db.session.commit()
