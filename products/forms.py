
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from django import forms
from .models import Review

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.friendly_name) for c in categories]


        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control' 


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'review_text', 'rating']

