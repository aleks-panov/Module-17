from django.shortcuts import render


# Create your views here.
def func_template(request):
    return render(request, 'func_template.html')