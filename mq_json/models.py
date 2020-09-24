import uuid
from django.db import models


class Message(models.Model):
    sender_uuid = models.ForeignKey(to='Client', related_name="sender_uuid_fk", on_delete=models.CASCADE)
    recipient_uuid = models.ForeignKey(to='Client', related_name="recipient_uuid_fk", on_delete=models.CASCADE)
    message = models.TextField()

class Client(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
