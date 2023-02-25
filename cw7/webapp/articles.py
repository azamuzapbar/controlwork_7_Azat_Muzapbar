from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Article
from webapp.form import ArticleForm

def add_article(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'add_article.html', context={'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                mail=form.cleaned_data['mail'],
                text=form.cleaned_data['text'],
            )
            return redirect(reverse('index'))
        else:
            return render(request, 'add_article.html', context={'form': form})

def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(initial={
            'title': article.title,
            'mail': article.mail,
            'text': article.text
        })
        return render(request, 'article_update.html', context={'form': form, 'article': article})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.mail = form.cleaned_data['mail']
            article.text = form.cleaned_data['text']
            article.save()
            return redirect(reverse('index'))
        else:
            return render(request, 'article_update.html', context={'form': form, 'article': article})


def article_delete(requst, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(requst, 'confirm.html', context={'article': article})


def confirm(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index')