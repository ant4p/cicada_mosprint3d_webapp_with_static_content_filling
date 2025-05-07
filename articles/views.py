from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ShowArticles(TemplateView):
    template_name = 'articles/articles.html'

class ShowArticle_1(TemplateView):
    template_name = 'articles/list/article_1.html'

class ShowArticle_2(TemplateView):
    template_name = 'articles/list/article_2.html'
