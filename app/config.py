from os import environ
from dotenv import load_dotenv

load_dotenv()
SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
COOKIES_PER_PAGE = 4
SECRET_KEY = environ.get("SECRET_KEY")
