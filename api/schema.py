from pydantic import BaseModel,EmailStr
from typing import Optional,List
from datetime import datetime 

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True

class NoteBase(BaseModel):
    title: str
    content: str
    tags: Optional[str] = None
    status: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[str] = None
    status: Optional[str] = None
    shared_with : Optional[List[int]] = None  # List of user IDs to share the note with

class NoteOut(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    tags: Optional[str] = None
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ShareNote(BaseModel):
    note_id: int
    user_id: int
    read_only: bool = True  

class ShareNoteOut(BaseModel):
    id: int
    note_id: int
    user_id: int
    read_only: bool

    class Config:
        from_attributes = True


class ShareNoteRequest(BaseModel):
    note_id: int
    target_user_id: int

    

