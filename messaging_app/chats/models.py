import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    """
    Custom user model using UUID as primary key and includes phone number.
    """
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=20, unique=True)

    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.email


class Conversation(models.Model):
    """
    Represents a conversation between users.
    """
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')

    def __str__(self):
        return self.title


class Message(models.Model):
    """
    A message sent by a user in a conversation.
    """
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.email} at {self.sent_at}"
