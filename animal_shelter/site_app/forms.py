from django import forms
from .models import Recall, Comment

class RecallFrom(forms.ModelForm):
    class Meta:
        model = Recall
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"