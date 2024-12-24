from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, "main_page.html")


def shop(request):
    return render(request, "shop.html")


def basket(request):
    return render(request, "basket.html")