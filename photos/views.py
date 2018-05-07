from django.shortcuts import render
from .models import Image
# Create your views here.


def photo_list(request):
    queryset = Image.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, "index.html", context)
