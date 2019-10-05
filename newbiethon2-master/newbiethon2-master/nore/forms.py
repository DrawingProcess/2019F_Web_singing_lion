from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'content', 'norebang', 'genre', 'number', 'ages']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '제목을 입력하세요.',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '내용을 입력하세요.',
                }
            ),
            'norebang': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'genre': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '방 이름/번호를 입력하세요.'
                }
            ),
            'ages': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
