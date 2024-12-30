from django import forms
from . import models


class Create_Article(forms.ModelForm):
    class Meta:
        model = models.article
        fields = ['title' , 'body' , 'slug' , 'thumb']
