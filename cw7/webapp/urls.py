from django.urls import path
from webapp.views import index_view
from webapp.articles import add_article
from webapp.articles import article_update
from webapp.articles import article_delete
from webapp.articles import confirm

urlpatterns = [
    path('', index_view, name='index'),
    path('article/', index_view),
    path('article/add/', add_article, name='article_add'),
    path('article/<int:pk>/update/', article_update, name='article_update'),
    path('article/<int:pk>/delete/', article_delete, name='article_delete'),
    path('article/<int:pk>/delete/confirm', confirm, name='confirm')
]