from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .forms import RegisterForm

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
        text = request.POST['username'] + request.POST['password']

        return HttpResponse(text)

