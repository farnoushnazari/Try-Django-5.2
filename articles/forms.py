from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'{title} is already in use.')
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        if title.lower().strip() == 'the officer':
            self.add_error('title', 'This title is taken!')
        return cleaned_data