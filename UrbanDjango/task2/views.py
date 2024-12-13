from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def func(request):
    return render(request, "func_template.html")

def main_page(request):
    return render(request, "main_page.html")

class Classes(TemplateView):
    template_name = "class_template.html"

