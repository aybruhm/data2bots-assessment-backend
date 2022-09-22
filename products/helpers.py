# Django Imports
from django.db import models

# Native Imports
import uuid


class ObjectTracker(models.Model):
    
    # ids
    id = models.BigAutoField(primary_key=True, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, help_text="Object unique ID.", editable=False)
    
    # datetime fields
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True