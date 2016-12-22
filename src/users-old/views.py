from django.shortcuts import render, redirect
from django.views import View, generic
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .forms import RegisterForm
from django.core.mail import EmailMessage
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login


class UserFormView(View):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # izvrsi registraciju
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user.set_password(password)
            user.save()

class Registration(View):
    def get(self, request, *args, **kwargs):
        the_form = RegisterForm()
        context = {
            "title": "BOKTE MAZO",
            "register": "BOKTE MAZO 223",
            "form": the_form
        }

        #msg = EmailMessage('Cao', 'Bok!', to=['jelaca.marko@ymail.com'])
        #msg.send()

        return render(request, 'users/register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = User.objects.get_or_create(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

            return HttpResponse(user.first_name)


        #msg = EmailMessage('Cao', 'Bok!', to=['volaric.ana@gmail.com'])
        #msg.send()

        return HttpResponse("Nije uspelo")

