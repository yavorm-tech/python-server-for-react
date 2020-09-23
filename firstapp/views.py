from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Credential
from django.shortcuts import render

# Create your views here.

def first(request):
    credentials = Credential.objects.all()
    return render(request, 'first_temp.html', {'credentials': credentials});

class Another(View):
    credentials = Credential.objects.all()
    output = ''
    for site in credentials:
        output += f"We have {site.name} and url {site.url}"
    def get(self, request):
        return HttpResponse(self.output)