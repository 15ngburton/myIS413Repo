from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect
from formlib import Formless

@view_function
def process_request(request):
    # process the form
    form = LoginForm(request)
    if form.is_valid():
        form.commit()
        #work of the form - create user, login user, purchase
        return HttpResponseRedirect("/")
    # render the form
    context = {
        "form": form,
    }
    return request.dmp_render('login.html', context)

class LoginForm(Formless):

    def init(self):
        self.fields['email'] = forms.CharField(label = "Email")
        self.fields['password'] = forms.CharField(label = "Password")

    def clean(self):
        self.user = authenticate(email=self.cleaned_data.get("email"), password=self.cleaned_data.get("password"))
        if self.user is None
            raise forms.ValidationError("Invalid Email or Password")
        return self.cleaned_data

    def commit(self):
        '''Process the form action'''
        login(self.request, self.user)
