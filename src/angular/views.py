import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404

from django.views.generic import View
from django.shortcuts import render

class AngularTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        print('ITEM:', item)
        template_dir_path = settings.TEMPLATES[0]["DIRS"][0]
        final_path = os.path.join(template_dir_path, "angular", "partials", item + ".html")

        try:
            html = open(final_path)
            return HttpResponse(html)
        except:
            raise Http404