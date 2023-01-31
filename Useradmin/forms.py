from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Row, Div, Submit
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class MySignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = (
            'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'profile_picture', 'some_file', 'password1',
            'password2')
    # password ist wegen UserCreationForm schon mit dabei
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group mx-1'),
                Column('last_name', css_class='form-group mx-1'),
            ),
            Row(
                Column('username', css_class='form-group mx-1'),
                Column('email', css_class='form-group mx-1'),
            ),
            Row(
                Column('date_of_birth', css_class='form-group mx-1'),
                Column('profile_picture', css_class='form-group mx-1'),
                Column('some_file', css_class='form-group mx-1'),
            ),
            Row(
                Column('password1', css_class='form-group mx-1'),
                Column('password2', css_class='form-group mx-1'),
            ),
            Div(
                Submit('submit', 'Signup', css_class='btn mx-auto'),
                css_class='text-center mb-5'
            )
        )
