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


class EnquiryForm(forms.Form):

    email = forms.EmailField()
    name = forms.CharField()
    phone = forms.CharField()
    # number_of_nights = forms.IntegerField()
    # number_of_people = forms.IntegerField()
    # ideal_month = forms.CharField()
    # ideal_dates = forms.CharField()


    # date = forms.DateField()
    
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            
            'email': 'Email Address',
            'name': 'Name',
            'phone': 'Phone Number',
            'message': 'Message',
            # 'postcode': 'Postal Code',
            # 'town_or_city': 'Town or City',
            # 'street_address1': 'Street Address 1',
            # 'street_address2': 'Street Address 2',
            # 'county': 'County, State or Locality'
        }
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'name':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
