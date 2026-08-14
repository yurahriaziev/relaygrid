from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

from uuid import uuid4, UUID

class Base(DeclarativeBase):
    pass

class Agent(Base):
    __tablename__ = 'agents'

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    name: Mapped[str] = mapped_column(String(100))
    agent_type: Mapped[str] = mapped_column(String(50))