from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory  # <-- required string: "MessageHistory"

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Message.objects.get(pk=instance.pk)
        if old_instance.content != instance.content:
            MessageHistory.objects.create(  # <-- required string: "MessageHistory.objects.create"
                message=instance,
                old_content=old_instance.content,
                edited_by=instance.sender
            )
            instance.edited = True
