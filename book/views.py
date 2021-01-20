from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect


# Create your views here.

DATA = [
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]


# for the models data
# from .models import ...

def home(request):
    data = { 'books': book.objects.all() }
    return render(request, 'book/home.html', data)


def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, 'book/404.html', data)

