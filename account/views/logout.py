from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.contrib.auth import logout

@view_function
def process_request(request):
        logout(request)
    return request.dmp_render('index.html', context)
