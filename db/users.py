from datetime import datetime

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy import Column, Table, Integer, String, DateTime

from db.base import metadata

Users = Table('Users', metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String(16), nullable=False),
              Column('email', String(60), unique=True, nullable=False),
              Column('password', String(500), nullable=False),
              Column('register_date', DateTime, default=datetime.utcnow())
              )


class BookSchema(SQLAlchemySchema):
    class Meta:
        model = Users
        load_instance = True

    id = auto_field()
    username = auto_field()
    email = auto_field()
    register_date = auto_field()
