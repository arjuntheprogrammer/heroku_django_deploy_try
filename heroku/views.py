from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the heroku index.")

def index(request):
    return render(request, "index.html", {})
