from django.shortcuts import render
from webapp.models import Article


def index_view(request):
    articles = Article.objects.exclude(status='blocked').order_by('-datetime')
    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)
