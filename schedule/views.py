from django.shortcuts import render
from django.views.generic.base import View
from django.template.context_processors import request

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'schedule/index.html', {'username' : request.user.username})


