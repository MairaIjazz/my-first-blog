from django import forms
from blogs.models import Post

class Postform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)