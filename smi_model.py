from sqlalchemy import String, Column, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class SMI(Base):
    __tablename__ = "tbl_webbid"

    webID: Mapped[int] = mapped_column(primary_key=True)
    stHash: Mapped[str] = Column(Text, nullable=False)
    ECGAINS: Mapped[str] = mapped_column(String(50), nullable=False)
    stBidNo: Mapped[str] = mapped_column(String(100), nullable=False)
    stTitle: Mapped[str] = mapped_column(String(250), nullable=False)
    txtDescription: Mapped[str] = mapped_column(String(250), nullable=False)
    stdtDueDate: Mapped[str] = mapped_column(String(100), nullable=False)
    stURL1: Mapped[str] = Column(Text, nullable=False)
    stURL2: Mapped[str] = Column(Text, nullable=False)
    stModuleName: Mapped[str] = mapped_column(String(100), nullable=False)
    stFileName: Mapped[str] = mapped_column(String(200), nullable=False)
    stFileCloudURL: Mapped[str] = mapped_column(String(400), nullable=False)
    iConverted: Mapped[int] = mapped_column(Integer(), nullable=False)
    stFileSize: Mapped[str] = mapped_column(String(50), nullable=False)