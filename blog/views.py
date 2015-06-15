# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from models import Post, Subscribe


class AuthMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthMixin, self).dispatch(*args, **kwargs)


class Feed(AuthMixin, ListView):
    model = Post
    ordering = '-created'

    def get_queryset(self):
        # TODO: optimize
        authors = set([o.author for o in Subscribe.objects.filter(
            reader=self.request.user)])
        return Post.objects.filter(author__in=authors)


class PostCreate(AuthMixin, CreateView):
    success_url = reverse_lazy('blog-index')
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


class SubscribeCreate(AuthMixin, CreateView):
    success_url = reverse_lazy('blog-index')
    model = Subscribe
    fields = ['author', ]

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super(SubscribeCreate, self).form_valid(form)


class Unsubscribe(AuthMixin, DeleteView):
    success_url = reverse_lazy('blog-index')
    model = Subscribe

    def get_object(self):
        return Subscribe.objects.get(
            author=self.kwargs.get('author_pk', None),
            reader=self.request.user,
        )


class MarkPostAsRead(AuthMixin, UpdateView):
    success_url = reverse_lazy('blog-index')
    model = Post
    fields = []

    def form_valid(self, form):
        form.instance.reads.add(self.request.user)
        return super(MarkPostAsRead, self).form_valid(form)
