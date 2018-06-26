from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogpage(request):
    context = {"blogs": Blog.objects}
    return render(request,"blog.html",context)