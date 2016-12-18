from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .forms import RegisterForm
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Gost

# Create your views here.
class Registration(View):
    def get(self, request, *args, **kwargs):
        the_form = RegisterForm()
        context = {
            "title": "BOKTE MAZO",
            "register": "BOKTE MAZO 223",
            "form": the_form
        }
        return render(request, 'users/register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        data = 'he he heheh heheh :P'

        new_user = User.objects.get_or_create(username=form.username, password=form.password, email=form.email )
        # send_mail('Cao mala', data, 'dejan@kuzmanovicd.com', ['volaric.ana@gmail.com'])
        return HttpResponse(data)

