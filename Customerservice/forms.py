from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Div, Submit, Row, Button
from django import forms
from Snacks.models import Snack, Comment


class SnackEditForm(forms.ModelForm):
    class Meta:
        model = Snack
        fields = ('name', 'gewicht', 'beschreibung', 'artikelnummer', 'preis', 'hersteller', 'bilder', 'produkt_info')

        # widgets = {
        #    'snack_id': forms.HiddenInput(),
        # }

    # def __init__(self, *args, **kwargs):
    #    widgets = {
    #        'snack_id': forms.HiddenInput(),
    #    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group  mx-auto'),
                Column('gewicht', css_class='form-group mx-auto'),
            ),
            Row(

                Column('beschreibung', css_class='form-group  mx-auto'),
            ),
            Row(
                Column('artikelnummer', css_class='form-group  mx-auto'),
                Column('preis', css_class='form-group mx-auto'),
                Column('hersteller', css_class='form-group mx-auto'),
            ),
            Row(

                Column('bilder', css_class='form-group  mx-auto'),
            ),
            Row(

                Column('produkt_info', css_class='form-group mx-auto'),
            ),
            Div(
                Submit('submit', 'Edit', css_class='btn mx-auto'),
                Submit('cancel', 'Cancel', css_class='btn-secondary mx-auto'),
                css_class='text-center'
            ),
        )


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'sternbewertung']
        widgets = {
            'sternbewertung': forms.Select(choices=Comment.STERN_BEWERTUNG),
            'comment_id': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        widgets = {
            'sternbewertung': forms.Select(choices=Comment.STERN_BEWERTUNG),
            'comment_id': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sternbewertung'].label = "Rating"
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Column('text', css_class='form-group  mx-auto'),
            Column('sternbewertung', css_class='form-group mx-auto'),

            Div(
                Submit('submit', 'Edit', css_class='btn mx-auto'),
                Submit('cancel', 'Cancel', css_class='btn-secondary mx-auto'),
                css_class='text-center'
            ),
        )
