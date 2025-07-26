from db.models import User, Note, SharedNote
from api.auth import hash_password, verify_password
from api.schema import NoteCreate, NoteUpdate 
from typing import Optional
from tortoise.queryset import Q

async def create_user(username:str ,email: str, password: str):
    user = await User.create(username=username, email=email, password=hash_password(password))
    return user

async def authenticate_user(email: str, password: str):
    user = await User.get_or_none(email=email)
    if not user or not verify_password(password, user.password):
        return None
    return user

async def get_other_users(current_user_id: int):
    return await User.filter(~Q(id=current_user_id)).all()
        
async def create_note(note_data: NoteCreate, user_id: int)-> Note:
    note = await Note.create(
        title=note_data.title,
        content=note_data.content,
        tags=note_data.tags,
        status=note_data.status,
        user_id=user_id
    )
    return note

async def update_note(note_id: int, note_data: NoteUpdate, user: User) -> Optional[Note]:
    note = await Note.get_or_none(id=note_id)
    if not note:
        return None

    # Mise à jour des champs
    update_data = note_data.dict(exclude_unset=True, exclude={"shared_with"})
    for key, value in update_data.items():
        setattr(note, key, value)

    await note.save()

    # Si le statut est "partagé", gérer les partages
    print("note")
    if note_data.status == "partagé" and note_data.shared_with is not None and len(note_data.shared_with) > 0:
        print(note_data.status)
        # Supprimer les partages précédents
        await SharedNote.filter(note=note).delete()
        print(f"Note {note.id} shared with users: ")

        for target_user_id in note_data.shared_with:
            if target_user_id != user["id"]:  # Exclure l'utilisateur courant
                target_user = await User.get_or_none(id=target_user_id)
                if target_user:
                    await SharedNote.create(note=note, user=target_user,read_only=True)

    return note


async def delete_note(note_id: int, user_id: int) -> bool:
    note = await Note.get_or_none(id=note_id, user_id=user_id)
    if not note:
        return False
    await note.delete()
    return True


async def get_all_notes(user_id: int, search: str | None = None, status: str | None = None):
    filters = Q(user_id=user_id)
    
    if search:
        filters &= (Q(title__icontains=search) | Q(tags__icontains=search))
    if status:
        filters &= Q(status=status)
    
    notes = await Note.filter(filters).all()
    return notes


async def fetch_note_by_id(note_id: int ,user_id: int) -> Optional[Note]:
    note = await Note.get_or_none(id=note_id,user_id=user_id)
    return note


async def get_shared_notes(user_id: int):
    shared_notes = await SharedNote.filter(user_id=user_id).prefetch_related('note')
    return [shared_note.note for shared_note in shared_notes]