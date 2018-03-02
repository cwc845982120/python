from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    user = models.Users.objects.get(pk=1)
    return render(request, 'website/index.html', {'user': user})
