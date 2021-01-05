from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': 'Назва категорії', 'required': 'required'}))
    category_order = forms.IntegerField(widget=forms.TextInput(attrs={'Порядок категорії у меню ': 'Електронна пошта',
                                                                      'required': 'required'}))
    is_visible = forms.BooleanField(widget=forms.CheckboxInput(attrs={ 'required': 'required'}))



    class Meta():
        model = Category
        fields = ('title', 'category_order', 'is_visible')
