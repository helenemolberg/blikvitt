import os

POSTGRES_LOCAL_BASE = 'postgresql://miljuser:miljuser@localhost:5432/'
DATABASE_NAME = 'miljo'
DATABASE_URI = os.getenv('DATABASE_URL', POSTGRES_LOCAL_BASE + DATABASE_NAME)
