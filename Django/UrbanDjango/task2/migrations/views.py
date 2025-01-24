from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func_templates(request):
    return render(request, "func_template.html")


class class_templates(TemplateView):
    template_name = 'class_templates'