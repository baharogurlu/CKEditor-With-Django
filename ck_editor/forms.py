from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from ck_editor.models import Post

class PostForm(forms.ModelForm):
    #content = forms.CharField(widget=CKEditorWidget(), label='Post')
    #content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'contentEditable': 'true'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Post
        fields = "__all__"