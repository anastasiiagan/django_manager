from django import forms
from .models import Publication
'''from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()'''

'''class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = (
            'client',
            'title',
            'content',
            'likes',
            'dislikes',
        )
    title = forms.CharField()
    content = forms.TextField()
    likes = forms.IntegerField(min_value=0)'''

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ['likes', 'dislikes', 'client',]