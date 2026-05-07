from django import forms
from .models import Book , Student , Student2 , Document

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = '__all__'


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
        widgets = {
            'pubdate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }