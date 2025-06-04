from rest_framework import serializers
from .models import CustomUser, Conversation, Message

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'bio', 'is_online'
        ]


class MessageSerializer(serializers.ModelSerializer):
    # sender will be represented as nested user, no manual CharField or SerializerMethodField
    sender = CustomUserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']
