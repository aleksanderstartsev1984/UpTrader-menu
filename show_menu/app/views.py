from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html', {'content': 'index'})


def page1(request):
    return render(request, 'app/page1.html', {'content': 'page1'})


def page2(request):
    return render(request, 'app/page2.html', {'content': 'page2'})


def page3(request):
    return render(request, 'app/page3.html', {'content': 'page3'})


def page4(request):
    return render(request, 'app/page4.html', {'content': 'page4'})
