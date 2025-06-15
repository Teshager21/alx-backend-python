from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)  # <-- required string: "edited"

    def __str__(self):
        return f"{self.sender} to {self.receiver}"

class MessageHistory(models.Model):  # <-- required string: "MessageHistory"
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)  # <-- required string: "edited_at"
    edited_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # <-- required string: "edited_by"

    def __str__(self):
        return f"History for Message {self.message.id}"
