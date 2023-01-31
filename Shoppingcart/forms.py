from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Div, Submit, Row, Button
from django import forms

from .models import Payment, ShoppingCartItem


class PaymentForm(forms.ModelForm):


    class Meta:
        model = Payment
        fields = ['kreditkartenr', 'ablaufsdatum', 'betrag']
        widgets = {
            'benutzer': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['betrag'].widget.attrs['readonly'] = True
        self.fields['kreditkartenr'].label = "Card number"
        self.fields['ablaufsdatum'].label = "Expiry date"
        self.fields['betrag'].label = "Total amount"
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Column('kreditkartenr', css_class='form-group col-4 mx-auto'),
            Column('ablaufsdatum', css_class='form-group col-4 mx-auto'),
            Column('betrag', css_class='form-group text-center col-3 mx-auto'),
            FormActions(
                Submit('cart', 'Pay', css_class='btn-success my-1 mx-1'),
                css_class='mx-3 mb-2',
            ),


        )


class AddForm(forms.ModelForm):
    class Meta:
        model = ShoppingCartItem
        fields = ['menge']
        widgets = {
            'produkt_id': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menge'].label = "Quantity"
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('menge', css_class='form-group'),
                Column(
                    Submit('cart', '+ Add to shopping cart', css_class='btn my-auto mx-1')
                    , css_class='mx-3 my-auto',
                )
            )
        )
