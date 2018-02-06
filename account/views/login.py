from django_mako_plus import view_function
from django import forms
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    # process the form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            #work of the form - create user, login user, purchase
            return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    # render the form
    context = {
        "form": form,
    }
    return request.dmp_render('formtest.html', context)

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput(),
    }
