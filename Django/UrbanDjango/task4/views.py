from django.shortcuts import render


# Create your views here.
def menu(request):
    return render(request, "fourth_task/menu.html")


def shop(request):
    games = ["Тетрис", "Змейка", "Волк ловит яйца"]
    context = {'games': games}
    return render(request, "fourth_task/shop.html", context)


def basket(request):
    cont = ["Извините, ваша корзина пуста"]
    context = {'cont': cont}
    return render(request, "fourth_task/basket.html", context)