#
#  Import LIBRARIES
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Session create_engine, select
#  Import FILES

#  ______________________



class Note(SQLModel, table=True) :
    id: int|None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    content: str
    is_done: bool = Field (default=False, index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc), 
        index=True)


class NoteCreate (SQLModel):
    title: str 
    content: str


class NoteUpdate (SQLModel):
    title: str | None = None
    content: str | None = None
    is_done: str | None = None