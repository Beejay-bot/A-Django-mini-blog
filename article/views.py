from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import article
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def index(request):
    art = article.objects.all()
    display_art = {'article': art}
    return render(request, 'index.html', display_art)


def blog(request, slug):
    if User.is_authenticated:
        # METHOD ONE: OF ROUTING THE ARTICLES UNIQUELY
        try:
            obj = article.objects.get(slug=slug)
        except article.DoesNotExist:
            raise Http404
        context = {
            'blog': obj
        }
        return render(request, 'blog.html', context)

        # METHOD TWO : OF DYNAMICALLY ROUTING THE ARTICLES. This is the preferred method.
        # return render_to_response('blog.html', {
        #     'blog': get_object_or_404(article, slug=slug)
        # })
    else:
        messages.error(request, ' Please log in before viewing article')
        return redirect('login')
