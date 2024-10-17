from sqlalchemy import Column, String, Integer, MetaData, Table

metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("name", String, primary_key=True, nullable=False),
    Column("password", String,  nullable=False),
)
