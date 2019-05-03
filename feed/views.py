from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from article.models import Article
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View




class FeedsView(generic.ListView):
    template_name = 'feed/index.html'
    context_object_name = 'all_articles'

    def get_queryset(self):
        return Article.objects.all()


class DetailView(generic.DetailView):
    model = Article
    template_name = 'article/article.html'



class ArticleCreate(CreateView):
    model = Article
    fields = ['article_title', 'article_text', 'article_image']

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['article_title', 'article_text', 'article_image']

class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('feed:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
