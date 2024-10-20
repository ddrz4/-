from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

class  NameStrPkMixin:
    name: Mapped[str] = mapped_column(primary_key=True, nullable=False)
