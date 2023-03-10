from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div
from django import forms

import Snacks.models
from .models import Snack, Comment


class SnackForm(forms.ModelForm):
    class Meta:
        model = Snack
        fields = ('name', 'gewicht', 'beschreibung', 'bilder', 'artikelnummer', 'preis', 'produkt_info')
        widgets = {
            'hersteller': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Column('name', css_class='form-group col-md-3 mx-auto'),
            Column('gewicht', css_class='form-group col-md-3 mx-auto'),
            Column('beschreibung', css_class='form-group col-md-3 mx-auto'),
            Column('artikelnummer', css_class='form-group col-md-3 mx-auto'),
            Column('preis', css_class='form-group col-md-3 mx-auto'),
            Column('bilder', css_class='form-group col-md-3 mx-auto'),
            Column('produkt_info', css_class='form-group col-md-3 mx-auto'),
            Div(
                Submit('submit', 'Add new snack', css_class='btn mx-auto'),
                css_class='text-center'
            )
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'sternbewertung']
        widgets = {
            'sternbewertung': forms.Select(choices=Comment.STERN_BEWERTUNG),
            'poster': forms.HiddenInput(),
            'snack': forms.HiddenInput(),
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
                Submit('comment', 'Post comment', css_class='btn mx-auto'),
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
                Submit('cancel', 'Cancel', css_class='btn mx-auto'),
                css_class='text-center'
            ),
        )


class SearchForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name',}), required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description',}), required=False)
    #produkt_bewertung = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Bewertung'}), required=False)
    #produkt_bewertung = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Bewertung'}), required=False)
    rating = forms.FloatField(widget=forms.Select(choices=Comment.STERN_BEWERTUNG, attrs={'placeholder': 'Rating'}), required=False)
    #rating = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Rating'}), required=False)
    # name = forms.CharField()
    # beschreibung = forms.CharField(required=False)
    # produkt_bewertung = forms.DecimalField(required=False)
    class Meta:
        model = Snack
        fields = ['name', 'beschreibung', 'produkt_bewertung']

    def __init__(self, *args, **kwargs):
        widgets = {
            'produkt_bewertung': forms.Select(choices=Comment.STERN_BEWERTUNG),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Column('name', css_class='form-group mx-1 my-auto pt-3'),
            Column('description', css_class='form-group mx-1 my-auto pt-3'),
            Column('rating', css_class='form-group mx-1 my-auto pt-3'),
            Div(
                Submit('submit', 'Search', css_class='btn my-auto mx-1')
                , css_class='mx-3 my-auto',
            )
        )
