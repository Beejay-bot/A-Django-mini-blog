from django.shortcuts import render
from .models import Author
# Create your views here.


def aboutme_view(request):
    content = Author.objects.all()
    display_content = {'author': content }
    return render(request, 'aboutme.html', display_content)