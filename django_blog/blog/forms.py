from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagField, TagWidget  # New imports for tagging
from .models import Profile, Post, Comment

# User Authentication Forms (unchanged)
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'website_url']

# Updated Blog Post Form with Tagging
class PostForm(forms.ModelForm):
    tags = TagField(
        required=False,
        widget=TagWidget(attrs={
            'class': 'form-control',
            'placeholder': 'Add comma-separated tags'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'featured_image', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your post content here...'
            }),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'featured_image': 'Featured Image (optional)'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['featured_image'].required = False
        self.fields['status'].label = 'Post Status'

# Comment Form (unchanged)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ''