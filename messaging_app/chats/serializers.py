from rest_framework import serializers
from .models import CustomUser, Conversation, Message

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'user_id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'bio', 'is_online'
        ]
        read_only_fields = ['user_id', 'is_online']  # you can adjust as needed


class MessageSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer(read_only=True)  # nested user info for sender

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)  # nested list of users
    messages = MessageSerializer(many=True, read_only=True)  # nested list of messages in conversation

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']
