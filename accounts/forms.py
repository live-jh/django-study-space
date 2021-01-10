from django import forms
from django.contrib.auth.forms import AuthenticationForm

from accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'address',
            'zipcode',
        ]


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3 * 3 = ?')

    #clean_message 인스타그램 form 참고
    def clean_answer(self):
        answer = self.cleaned_data.get('answer')
        if answer != 9:
            raise forms.ValidationError("u r wrong r u stupid")
        return answer