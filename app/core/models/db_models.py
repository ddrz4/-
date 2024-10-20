from sqlalchemy import Column, String, Integer, MetaData, Table, Boolean, DateTime  
from datetime import datetime

metadata = MetaData()


# user = Table(
#     "user",
#     metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True, nullable=False),
#     Column("name", String, primary_key=True, nullable=False),
#     Column("email", String, nullable=False),
#     Column("hashed_password", String,  nullable=False),
#     Column("is_active", Boolean, nullable=False, default=False),
#     Column("is_verified", Boolean, nullable=False, default=False),
#     Column("is_superuser", Boolean, nullable=False, default=False),
# )

accesstoken = Table(
    "accesstoken",
    metadata,
    Column("token", String(length=43), primary_key=True, nullable=False),
    Column("created_at", DateTime, nullable=False, default=datetime.now),
    Column("user_id", Integer, nullable=False),
)

# token: Mapped[str] = mapped_column(
#         String(length=43),
#         primary_key=True,
#         nullable=False
#     )
#     created_at: Mapped[datetime] = mapped_column(
#             TIMESTAMPAware(timezone=True),
#             nullable=False
#         )
#     user_id: Mapped[UserIdType] = mapped_column(
#         Integer,
#         ForeignKey("user.id", ondelete="cascade"),
#         nullable=False
#     )