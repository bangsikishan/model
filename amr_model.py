from .shared_libs import *

class Base(DeclarativeBase):
    pass

class AMR(Base):
    __tablename__ = "tbl_bid_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    agency_ecgain: Mapped[str] = mapped_column(String(25), nullable=False)
    number: Mapped[str] = mapped_column(String(50), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    brodcast_date: Mapped[str] = mapped_column(String(50), nullable=False)
    due_date: Mapped[str] = mapped_column(String(50), nullable=False)
    hash_value: Mapped[str] = mapped_column(String(1000), nullable=False)
    url1: Mapped[str] = mapped_column(String(500), nullable=False)
    url2: Mapped[str] = mapped_column(String(500), nullable=False)