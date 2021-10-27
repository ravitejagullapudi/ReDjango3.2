from django import forms
from django.forms import fields

from .models import Article


class ArticleFormOld(forms.Form):
    title = forms.CharField(max_length=250)
    content = forms.CharField(widget=forms.Textarea)

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if(title.lower().strip() == "the office"):
    #         raise forms.ValidationError('This title is already taken')

    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print("All data", cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if(title.lower().strip() == "the office"):
            self.add_error('title','This title is taken.')
            # raise forms.ValidationError('This title is already taken')
        if "office" in content:
            self.add_error('content','Office cannot be in content')
            raise forms.ValidationError("office is not valid in content")
        return cleaned_data

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.all().filter(title__icontains = title)
        if(qs.exists()):
            self.add_error("title",f"\"{title}\" is already in use.")
        return data
