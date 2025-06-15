from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

@receiver(post_save, sender=Message)
def new_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(message=instance)


@receiver(pre_save, sender=Message)
def edit_message(sender, instance, **kwargs):
    if instance.pk:
        old = Message.objects.get(pk=instance.pk)
        if old.content != instance.content:
            MessageHistory.objects.create(
                message = instance,
                content = old.content,
                edited_by = instance.sender
            )
            instance.edited = True

@receiver(post_delete, sender=User)
def user_data_cleanup(sender, instance, **kwargs):
    Message.objects.filter(Q(sender=instance) | Q(receiver=instance)).delete()
    MessageHistory.objects.filter(edited_by=instance).delete()
    Notification.objects.filter(Q(recipient=instance) | Q(sender=instance)).delete()
