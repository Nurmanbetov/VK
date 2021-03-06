from django import forms
from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["to_user", "chat"]


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ["name"]


