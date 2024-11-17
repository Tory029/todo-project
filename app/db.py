
from datetime import datetime
from sqlalchemy import String, TIMESTAMP, select
from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker, 
                                    AsyncSession) 
from sqlalchemy.orm import (declarative_base, Mapped, mapped_column)


DATABASE_URL = 'postgresql+asyncpg://localhost:5432/postgres'
#async engine to work with database
engine = create_async_engine(url=DATABASE_URL, echo=True)
Base = declarative_base()
# fabric of session to communicate with database
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# Todo table
class Todo(Base):
    __tablename__ = 'Todos',

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(40), nullable=False)
    content: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=False), nullable=False)
    closed_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=False), nullable=False)

#create the database
Base.metadata.create_all(engine)


async def init_models():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

# session create
async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session



