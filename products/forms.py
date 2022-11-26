from django import forms

class ProductCreateForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()

class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=10, max_length=1000)