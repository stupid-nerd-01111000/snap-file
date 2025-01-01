from django.db import models
import uuid


class FileTransfer(models.Model):
    file = models.FileField(upload_to='uploads/')
    code = models.CharField(max_length=8, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)