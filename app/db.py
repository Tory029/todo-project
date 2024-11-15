from datetime import datetime
from sqlalchemy import String, DateTime, select
from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker, 
                                    AsyncSession) 
from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column)


DATABASE_URL = 'postgresql+asyncpg://localhost:5432/postgres'
#async engine to work with database
engine = create_async_engine(url=DATABASE_URL)

# fabric of session to communicate with database
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# Todo table
class Todo(DeclarativeBase):
    __tablename__ = 'Todos',

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(40))
    content: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime)


def connecion(method):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session: # auto open and close
                                                     # session in async
            try:
                return await method(*args, session, **kwargs)
            except Exception as E:
                await session.rollback() #open session while errore
                raise E # return Exception
            finally:
                await session.close() # close session


    return wrapper

@connecion
async def get_todos(session):
    return await session.execut(select(Todo))
