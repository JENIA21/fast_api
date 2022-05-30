import sqlalchemy

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('email', sqlalchemy.String(40), unique=True, index=True),
    sqlalchemy.Column('user_name', sqlalchemy.String(100)),
    sqlalchemy.Column('user_data', sqlalchemy.String()),
    sqlalchemy.Column('password', sqlalchemy.String()),
    sqlalchemy.Column('date', sqlalchemy.DateTime),
)


