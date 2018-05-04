from django.shortcuts import render
from .models import Photo
# Create your views here.


def photo_list(request):
    queryset = Photo.object.all()
    context = {
        "photos": queryset,
    }
    return render(request, "photo.html", context)
