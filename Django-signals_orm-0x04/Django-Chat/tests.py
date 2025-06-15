from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, MessageHistory

class MessageEditSignalTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='sender', password='pass')
        self.receiver = User.objects.create_user(username='receiver', password='pass')
        self.message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Original message"
        )

    def test_edit_logs_history(self):
        self.message.content = "Updated message"
        self.message.save()

        history = MessageHistory.objects.filter(message=self.message).first()
        self.assertIsNotNone(history)
        self.assertEqual(history.old_content, "Original message")
        self.assertTrue(self.message.edited)
