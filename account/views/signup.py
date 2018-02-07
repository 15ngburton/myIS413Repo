from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib import Formless
from account import models as amod

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
        self.fields['password2'] = forms.CharField(label = "Reenter Password")

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("Password is not long enough")
        if not (any(char.isdigit() for char in password)):
            raise forms.ValidationError("Password must contain a number")
        return password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        emailProxy = amod.User.objects.get(email = email)
        if not emailProxy:
            raise forms.ValidationError("Email already in system")

    def clean(self):
        password = self.cleaned_data.get("password")
        passwordX = self.cleaned_data.get("password2")
        if not (passwordX == password):
            raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data

    def commit(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        u1 = amod.User()
        u1.email = email
        u1.set_password(password)
        u1.save()
        self.user = authenticate(email=email, password=password)
        login(self.request, self.user)
