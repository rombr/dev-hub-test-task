# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=_(u'Автор'))
    title = models.CharField(_(u'Заголовок'), max_length=128)
    body = models.TextField(_(u'Текст записи'))
    created = models.DateTimeField(_(u'Дата добавления'), auto_now_add=True)

    reads = models.ManyToManyField(
        User, related_name='post_reader',
        verbose_name=_(u'Кто прочитал'), blank=True,
    )

    def __unicode__(self):
        return '%s: %s: %s' % (
            self.author, self.created, self.title,
        )

    class Meta:
        ordering = ['-created']
        verbose_name = _(u'Запись')
        verbose_name_plural = _(u'Записи')


class Subscribe(models.Model):
    author = models.ForeignKey(
        User, related_name='author', verbose_name=_(u'Автор'))
    reader = models.ForeignKey(
        User, related_name='reader', verbose_name=_(u'Читатель'))
    date_joined = models.DateField(_(u'Дата добавления'), auto_now_add=True)

    def __unicode__(self):
        return '%s reads %s since %s' % (
            self.reader, self.author, self.date_joined,
        )

    class Meta:
        unique_together = ('author', 'reader', )
        ordering = ['-date_joined']
        verbose_name = _(u'Подписка')
        verbose_name_plural = _(u'Подписки')


@receiver(post_save, sender=Post)
def create_post_handler(sender, **kwargs):
    if kwargs.get('created', False):
        post = kwargs['instance']
        readers = set([o.reader for o in Subscribe.objects.filter(
            author=post.author)])

        for o in readers:
            send_mail(
                _(u'Новая публикация'),
                unicode(post),
                'noreply@',
                [o.email],
                fail_silently=False,
            )
