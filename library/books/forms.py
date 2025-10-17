#form definition
from django import forms
# class BookForm(forms.Form):
#      title=forms.CharField()
#      author=forms.CharField()
#      pages=forms.IntegerField()
#      price=forms.IntegerField()
#      language=forms.CharField()


from books.models import Book
class BookForm(forms.ModelForm):
     class Meta:
          model=Book
          fields='__all__'


