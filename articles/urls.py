from django.urls import path

from articles.views import ShowArticles, ShowArticle_1, ShowArticle_2

app_name = 'articles'

urlpatterns = [
    path('',ShowArticles.as_view(), name='articles'),
    path('article_1/',ShowArticle_1.as_view(), name='article_1'),
    path('article_2/',ShowArticle_2.as_view(), name='article_2'),
]