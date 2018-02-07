from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib import Formless

@view_function
def process_request(request):
    # process the form
    form = TestForm(request)
    if form.is_valid():
        #work of the form - create user, login user, purchase
        return HttpResponseRedirect("/")
    # render the form
    context = {
        "form": form,
    }
    return request.dmp_render('formtest.html', context)

class TestForm(Formless):

    def init(self):
        self.fields['email'] = forms.CharField(label = "Email")
        self.fields['password'] = forms.CharField(label = "Password")
        self.fields['password2'] = forms.IntegerField(label = "Reenter Password")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("Password is not long enough")
        if not (any(char.isdigit() for char in password)):
            raise forms.ValidationError("Password must contain a number")
        return password
