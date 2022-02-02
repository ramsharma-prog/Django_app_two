from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'text', 'category')
        model = models.Post


class TagForm(forms.ModelForm):
    class Meta:
        fields = ('name',)
        model = models.Tag


class CommentForm(forms.ModelForm):
    class Meta:
        fields = ('comment_text',)
        model = models.Comment


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        fields = ('reply_text',)
        model = models.Reply
