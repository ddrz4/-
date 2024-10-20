from sqlalchemy import Column, String, Integer, MetaData, Table, Boolean

metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("name", String, primary_key=True, nullable=False),
    Column("email", String, nullable=False),
    Column("hashed_password", String,  nullable=False),
    Column("is_active", Boolean, nullable=False, default=False),
    Column("is_verified", Boolean, nullable=False, default=False),
    Column("is_superuser", Boolean, nullable=False, default=False),
)
