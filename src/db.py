from databases import Database

from config import Config

database = Database(Config.SQLALCHEMY_DATABASE_URI)
