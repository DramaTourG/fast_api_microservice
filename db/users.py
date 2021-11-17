from datetime import datetime

from sqlalchemy import Column, Table, Integer, String, DateTime

from db.base import metadata

Users = Table('Users', metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String(16), nullable=False),
              Column('email', String(60), unique=True, nullable=False),
              Column('password', String(500), nullable=False),
              Column('register_date', DateTime, default=datetime.utcnow())
              )
