from django.shortcuts import render
from gallery.models  import  Gallery

def home(request):
    gallerys = Gallery.objects
    context  = {"gallerys":gallerys}
    return render(request,"home.html",context)