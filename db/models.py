
from datetime import datetime
from enum import Enum
from tortoise import fields
from tortoise.models import Model
import uuid


class User(Model):
    id=fields.IntField(pk=True)
    username=fields.CharField(max_length=50, unique=True)
    email=fields.CharField(max_length=100, unique=True)
    password=fields.CharField(max_length=255)
    created_at=fields.DatetimeField(default=datetime.now)
    updated_at=fields.DatetimeField(auto_now=True)
    class Meta:
        table="users"
 

class Note(Model):
    id=fields.IntField(pk=True)
    user=fields.ForeignKeyField("models.User", related_name="notes", on_delete=fields.CASCADE)
    title=fields.CharField(max_length=255)
    content=fields.TextField()
    created_at=fields.DatetimeField(default=datetime.now)
    updated_at=fields.DatetimeField(auto_now=True)
    tags=fields.CharField(max_length=255, null=True,required=False)
    status=fields.CharField(max_length=255)
    shared_with = fields.ManyToManyField("models.User", related_name="shared_notes", through="shared_notes", on_delete=fields.CASCADE ,required=False)
    public_token = fields.CharField(max_length=100, null=True, unique=True,required=False)

    class Meta:
        table="notes"
    async def save(self, *args, **kwargs):
        # Si la note est "public" et qu'il n'y a pas encore de token, on en génère un
        if self.status == "public" and not self.public_token:
            self.public_token = str(uuid.uuid4())
        # Si la note n'est pas "public", on supprime le token
        elif self.status != "public":
            self.public_token = None
        await super().save(*args, **kwargs)

class SharedNote(Model):
    id = fields.IntField(pk=True)
    note = fields.ForeignKeyField("models.Note", related_name="shared_users", on_delete=fields.CASCADE)
    user = fields.ForeignKeyField("models.User", related_name="shared_users", on_delete=fields.CASCADE)
    read_only = fields.BooleanField(default=True)

    class Meta:
        table = "shared_notes"



