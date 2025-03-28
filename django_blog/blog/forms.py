from django import forms
from .models import Post
from taggit.forms import TagWidget
from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']  # include fields you want in the form

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if len(body) < 5:
            raise forms.ValidationError("Comment is too short! Minimum 5 characters.")
        return body
'''
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 3:
            raise forms.ValidationError('Comment must be at least 3 characters long.')
        return content
'''

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # <-- required for the check
        }
