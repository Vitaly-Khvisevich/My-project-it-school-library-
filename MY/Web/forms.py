from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import comments, book






class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
    def save(self, commit=True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class Create_book(forms.ModelForm):
    class Meta:
        model = book
        fields = ('book_name', 'author', 'series', 'brief_description', 'language', 'release_year', 'picture', 'files' )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"



class Add_comment(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('name', 'comment', 'score', 'book_id')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
            self.fields['name'].label='Имя пользователя'
            self.fields['comment'].widget=forms.Textarea(attrs={"class": "form-control"})
            self.fields['comment'].label='Комментарий'
            self.fields['score'].label='Оценка'
            self.fields['book_id'].required=False
            self.fields['book_id'].label='Номер книги'
    
    





            