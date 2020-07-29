from django import forms
from .widgets import CustomClearableFileInput
from .models import Campspot, Category


class CampspotForm(forms.ModelForm):
    """ form for add and edit_campspot view to allow superuser to add/edit.
    Allows authorised business user to edit campspot information easily """
    class Meta:
        model = Campspot
        # Quick fix for models allowing admin to make amendments for testing.
        exclude = ['motorhome_service_point']
        # Defensive design excludes user edit in the form so owner can not be changed.
        exclude = ['owner']
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    # changing field type without migration is very useful
    host_brief = forms.CharField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'