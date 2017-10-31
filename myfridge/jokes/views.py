from django.shortcuts import render

from .models import Joke

import markdown
import bleach

def index(request):
    return render(request, 'jokes/index.html', {
        "jokes": Joke.objects.all(),
        "user": request.user,
    })

def show_joke(request, id):
    joke = Joke.objects.get(id=id)
    text = bleach.clean(
        markdown.markdown(joke.text),
        tags=['h1', 'h2', 'strong', 'blockquote', 'p'],
    )
    print('Text:', text)
    return render(request, 'jokes/joke.html', dict(
        id=joke.id,
        text=text,
        author=joke.author.username
    ))
