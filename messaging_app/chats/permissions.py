# chats/permissions.py

from rest_framework import permissions  # ✅ REQUIRED IMPORT

class IsConversationParticipant(permissions.BasePermission):  # ✅ INHERITS BasePermission
    """
    Allows access only to participants of the conversation.
    """
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()


class IsMessageParticipant(permissions.BasePermission):  # ✅ INHERITS BasePermission
    """
    Allows access only if the user is a participant in the message's conversation.
    """
    def has_object_permission(self, request, view, obj):
        return request.user in obj.conversation.participants.all()
