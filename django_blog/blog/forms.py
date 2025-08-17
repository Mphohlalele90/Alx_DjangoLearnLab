from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post

# Existing authentication forms (unchanged)
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

# New form for blog post CRUD operations
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'featured_image']
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
        # Make the featured image field not required
        self.fields['featured_image'].required = False
        # Set a more user-friendly label for the status field
        self.fields['status'].label = 'Post Status'