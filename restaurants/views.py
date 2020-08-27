from django.shortcuts import render


def home(request):
    context = {
        "msg": "Hello World!",
    }
    return render(request, 'home_page.html', context)
