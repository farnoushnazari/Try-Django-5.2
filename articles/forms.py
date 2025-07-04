from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        if title.lower().strip() == 'the officer':
            self.add_error('title', 'This title is taken!')
        return cleaned_data