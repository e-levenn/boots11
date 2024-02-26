from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')


def main(request):
    return render(request, 'main.html')


def matches(request):
    return render(request, 'matches.html')


def players(request):
    return render(request, 'players.html')


def single(request):
    return render(request, 'single.html')


# Create your views here.
