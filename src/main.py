#
#  Import LIBRARIE
from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

#  Import FILES

#  ______________________


engine: Engine = create_engine(url="sqlite:///./notes.db", echo=True)


# Define the Lifespan (Startup + Shutdown logic)
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # --- Logic here runs BEFORE the app starts (Startup) ---
    SQLModel.metadata.create_all(bind=engine)

    yield  # The app stays "alive" while it's here

    # --- Logic here runs AFTER the app stops (Shutdown) ---
    # (e.g., closing database connections or clearing cache)


app = FastAPI(title="SQLModel Demo", lifespan=lifespan)


def get_session() -> Generator[Session, None, None]:
    """Provides a database session for a single request and closes it after."""
    with Session(engine) as session:
        yield session


# Building the APIs


@app.get(path="/")
def main() -> dict[str, str]:
    return {"message": "Hello World"}


# engine: Engine = create_engine(url= "sqlite:///./notes.db", echo=True)
# @app. on_event("startup")
# def on_startup() -> None :
#     SQLModel.metadata. create_all(engine)


#
#  Import LIBRARIE
#  Import FILES

#  ______________________
