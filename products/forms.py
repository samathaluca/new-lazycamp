from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ form for add and edit_product view to allow superuser to add/edit.
    Allows authorised business user to edit product information easily """
    class Meta:
        model = Product
        # Defensive design excludes user edit in the form so owner can not be changed.
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
    ''' Form for contact on contact.html'''
    email = forms.EmailField()
    name = forms.CharField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class EnquiryForm(ContactForm):
    ''' Subclass of ContactForm with additional fields 
    for booking Enquiry'''
    number_of_nights = forms.IntegerField()
    number_of_people = forms.IntegerField()
    ideal_month = forms.CharField()
    # dates availability enquiry set as CharField because often there are preferences to state. 
    ideal_dates = forms.CharField()
