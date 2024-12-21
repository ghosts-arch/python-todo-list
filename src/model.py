from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, Mapped, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Task(Base):

    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    label: Mapped[str] = mapped_column(nullable=False)
    is_completed: Mapped[bool] = mapped_column(default=False)


DATABASE_URL = "sqlite:///tasks.db"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base.metadata.create_all(engine)
