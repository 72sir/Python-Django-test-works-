# coding: utf-8
import re
from django.shortcuts import render


# Create your views here.


def index(request):

    if request.method == "POST":
        if request.POST['text']:
            str = request.POST['text']
        else:
            str = 'esdfd((esdf)(((((esdf)(esdf'
    else:
        str = 'esdfd((esdf)(((((esdf)(esdf'

    pattern = '^[a-zA-Z]*([(]*[a-zA-Z]*[)])*'  # Смотрим что из себя представлеят начало строки
    resultSearch = re.search(pattern, str)

    # Без регулярного выражения
    i = 0
    buf = ''
    char = ''
    for elem in str:
        if i == 0 and elem != '(':
            char = char + elem
        elif elem == '(' and buf is None:
            buf = elem
        elif elem == '(' and buf is not None:
            buf = buf + elem
        elif elem == ')':
            char = char + buf + elem
            buf = ''
        else:
            buf = buf + elem

        i += 1

    return render(request, 'index.html', {'resultSearch': resultSearch.group(), 'defaultStr': str, 'result': char})
