from django.template import Library
from django.contrib.auth.models import User
import django.contrib.auth

from lbforum.models import Topic, Category, Post

register = Library()


@register.inclusion_tag('lbforum/tags/dummy.html')
def lbf_categories_and_forums(forum=None, template='lbforum/widgets/categories_and_forums.html'):
    return {'template': template,
            'forum': forum,
            'categories': Category.objects.all()}


@register.inclusion_tag('lbforum/tags/dummy.html')
def lbf_status(template='lbforum/widgets/lbf_status.html'):
    return {'template': template,
            'total_topics': Topic.objects.count(),
            'total_posts': Post.objects.count(),
            'total_users': django.contrib.auth.get_user_model().objects.count(),
            'last_registered_user': django.contrib.auth.get_user_model().objects.order_by()[0]}
