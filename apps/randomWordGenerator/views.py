from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_word = get_random_string(length=14, allowed_chars=chars)
    context = {
        "word": random_word,
    }
    return render(request, 'randomWordGenerator/index.html', context)

def reset(request):
    del request.session['counter']
    return redirect("/random_word")
