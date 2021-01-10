from django import forms
from .models import Category, Dish


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': 'Назва категорії', 'required': 'required'}))
    category_order = forms.IntegerField(widget=forms.TextInput(attrs={'Порядок категорії у меню ': 'Електронна пошта',
                                                                      'required': 'required'}))
    is_visible = forms.BooleanField(widget=forms.CheckboxInput(attrs={'required': 'required'}))

    class Meta():
        model = Category
        fields = ('title', 'category_order', 'is_visible')


class DishForm(forms.ModelForm):
    # title = forms.CharField(max_length=50,
    #                         widget=forms.TextInput(attrs={'placeholder': 'Назва страви', 'required': 'required'}))
    # price = forms.DecimalField(max_digits=7, decimal_places=2,
    #                            widget=forms.NumberInput(attrs={'required': 'required'}))
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),
    #                                   widget=forms.Select(choices=Category.objects.all(),
    #                                   attrs={'required': 'required'}))
    # # category = forms.ModelChoiceField(queryset=Category.objects.all())
    #
    # description = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'required': 'required'}))
    # photo = forms.ImageField(required=False)
    # spicy = forms.BooleanField(widget=forms.CheckboxInput(attrs={'required': 'required'}))

    class Meta():
        model = Dish
        fields = ('title', 'price', 'category', 'description', 'photo', 'spicy')
