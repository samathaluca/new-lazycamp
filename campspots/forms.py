from django import forms
from .widgets import CustomClearableFileInput
from .models import Campspot, Category


class CampspotForm(forms.ModelForm):

    class Meta:
        model = Campspot
        exclude = ['motorhome_service_point']
        exclude = ['owner']
        # widgets = {
        #     'bare_all': forms.CharField()
        # }
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    host_brief = forms.CharField()
    # campspot_email = forms.EmailField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'