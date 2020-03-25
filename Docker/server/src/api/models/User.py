from . import db


class User(db.Model):
    __tablename__ = 'users'
    #__table_args__ = {'schema':'BB_ADM'}
  
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True,nullable=False)
    password = db.Column(db.String(80))
    email = db.Column(db.String(80), unique = True,nullable=False)

    def __init__(self, public_id, name, surname, username, password,email):
        self.public_id = public_id
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.email = email

    @property
    def serialize(self):
        return {'public_id': self.public_id, 'name': self.name, 'surname': self.surname, 'username': self.username, 'password': self.password, 'email': self.email, }
        
    def __repr__(self):
        return f'<User {self.name}>'