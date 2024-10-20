from sqlalchemy import create_engine
from app.core.models.db_models import metadata

sync_engine = create_engine(
   url="postgresql+psycopg://postgres:postgre@localhost:5432/owo",
   echo=True,
)

def create_table():
   metadata.create_all(sync_engine)

create_table()
