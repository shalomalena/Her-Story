from django import forms

from .models import Comment, Contact, Vent, VentComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }

class VentForm(forms.ModelForm):
    class Meta:
        model = Vent
        fields = ['author_name', 'author_email', 'title', 'content']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your name will not be shared'}),
            'author_email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Your email will not be shared'}),
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Your Story'}),
        }

class VentCommentForm(forms.ModelForm):
    class Meta:
        model = VentComment
        fields = ['content', 'commenter_name', 'commenter_email']
        widgets = {
            'commenter_email': forms.EmailInput(attrs={'placeholder': 'Your email will not be shared'}),
            'commenter_name': forms.TextInput(attrs={'placeholder': 'Your name will not be shared'}),
        }