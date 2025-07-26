from fastapi import APIRouter, Depends, HTTPException, Query
from api.schema import UserCreate, UserLogin, NoteUpdate,NoteCreate,NoteOut, ShareNoteRequest,UserOut
from db.models import Note, SharedNote
import uuid
from api.crud import create_user, authenticate_user,update_note, delete_note, create_note,get_all_notes,fetch_note_by_id,get_other_users,get_shared_notes
from api.auth import create_access_token, get_current_user
from db.models import User

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    user_obj = await create_user(user.username, user.email, user.password)
    token = create_access_token({"sub": user_obj.email})
    return {"access_token": token,
            "user": {
                "id":user_obj.id,
                "username": user_obj.username,
                "email": user_obj.email 
            }
            }

@router.post("/login")
async def login(user: UserLogin):
    user_obj = await authenticate_user(user.email, user.password)
    if not user_obj:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token=create_access_token(data={"id": user_obj.id, "email": user_obj.email})
    return {"access_token": access_token,
            "user": {
                "id": user_obj.id,
                "username": user_obj.username,
                "email": user_obj.email 
            }
            }
# Get all other users
@router.get("/users", response_model=list[UserOut])
async def get_users(current_user: User = Depends(get_current_user)):
    users = await get_other_users(current_user["id"])
    if not users:
        raise HTTPException(status_code=404, detail="No other users found")
    return users


# Adding routes for notes
@router.post("/notes", response_model=NoteOut)
async def add_note(note: NoteCreate, user: User = Depends(get_current_user)):
    return await create_note(note, user["id"])

# Update notes
@router.put("/notes/{note_id}", response_model=NoteOut)
async def edit_note(
    note_id: int,
    note: NoteUpdate,
    user: User = Depends(get_current_user)
):
    existing_note = await update_note(note_id, note_data=note, user=user)

    if not existing_note:
        raise HTTPException(status_code=404, detail="Note not found")

    return existing_note

# Delete notes
@router.delete("/notes/{note_id}")
async def remove_note(note_id: int,user: User = Depends(get_current_user)):
    deleted = await delete_note(note_id,user["id"])
    if not deleted:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"ok": True}

# Get all notes
@router.get("/notes", response_model=list[NoteOut])
async def get_notes_route(
    current_user: User = Depends(get_current_user),
    search: str | None = Query(None, description="Recherche par titre ou tags"),
    status: str | None = Query(None, description="Filtrer par statut"),
):
    notes = await get_all_notes(current_user["id"], search=search, status=status)
    if not notes:
        raise HTTPException(status_code=404, detail="No notes found")
    return notes


# Get note by ID
@router.get("/notes/{note_id}", response_model=NoteOut)
async def get_note_by_id(note_id: int, current_user: User = Depends(get_current_user)):
    note = await fetch_note_by_id(note_id, current_user["id"])
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post("/notes/share")
async def share_note(request: ShareNoteRequest, current_user: User = Depends(get_current_user)):
    note = await Note.get_or_none(id=request.note_id, user=current_user)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note.status = "partagé"
    await note.save()
    await SharedNote.create(note=note, user_id=request.target_user_id)
    return {"message": "Note shared"}

# Get shared notes
@router.get("/shared-notes", response_model=list[NoteOut])
async def get_shared_notes_route(current_user: User = Depends(get_current_user)):   
    shared_notes = await get_shared_notes(current_user["id"])
    if not shared_notes:
        raise HTTPException(status_code=404, detail="No shared notes found")
    return shared_notes
# Get public notes
@router.get("/public-note/{token}", response_model=NoteOut)
async def get_public_note(token: str):
    note = await Note.get_or_none(public_token=token, status="public")
    if not note:
        raise HTTPException(status_code=404, detail="Note non trouvée ou pas publique")
    return note

