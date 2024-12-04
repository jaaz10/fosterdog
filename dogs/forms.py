from django import forms
from .models import Dog

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'gender', 'size', 'description', 'photo', 'needs_foster']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class QuickUploadForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'photo', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about this dog...'}),
            'name': forms.TextInput(attrs={'placeholder': "Dog's name"})
        }
