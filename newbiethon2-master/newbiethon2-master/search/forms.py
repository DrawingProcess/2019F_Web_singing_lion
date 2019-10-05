from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목으로 검색하세요.'}))
    # GENRES = [('힙합', '힙합'), ('발라드', '발라드'), ('팝송', '팝송'), ('R&B', 'R&B'), ('댄스', '댄스'), ('락', '락')]
    genre = forms.CharField(max_length=10,required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '장르로 검색하세요.'}))
    # AGES = [('10대', '10대'), ('20대', '20대'), ('30대', '30대'), ('40대', '40대'), ('50대', '50대')]
    ages = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '연령대로 검색하세요.'}))
    