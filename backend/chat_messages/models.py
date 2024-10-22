from django.db import models
from date.models import Date
from conversation.models import Conversation
from django.utils.translation import gettext_lazy as _

class Message(Date):
    class Sender(models.TextChoices):
        AI = "AI"
        SYSTEM = "SYSTEM"
        HUMAN = "HUMAN"

    related_conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.CharField(max_length=6, choices=Sender)
    message_content = models.TextField()

    def __str__(self):
        return f'{self.sender}: {self.message_content[:30]}'