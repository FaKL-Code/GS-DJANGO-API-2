from django import forms

from .models import Doacao


class DoacaoForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Doacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DoacaoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['is_done'].widget.attrs['class'] = None
