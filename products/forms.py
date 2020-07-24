from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['owner']

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ContactForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)



class EnquiryForm(ContactForm):


    number_of_nights = forms.IntegerField()
    number_of_people = forms.IntegerField()
    ideal_month = forms.CharField()
    ideal_dates = forms.CharField()
    
    # date = forms.DateField()
