from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Registration(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title": "BOKTE MAZO",
            "register": "BOKTE MAZO 223"
        }
        return render(request, 'users/register.html', context)



