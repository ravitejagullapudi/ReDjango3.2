'''
Main Purpose of this file is to render html webpages
'''

from articles.models import Article
from django.http import HttpResponse
from django.template.loader import render_to_string


def home(request):
    """Take in a request (Django sends request) and return html response (We pick to return the response)"""
    name = "Ravi"
    article_obj = Article.objects.get(id=3)
    article_querySet = Article.objects.all()
    context = {
        "title": article_obj.title,
        "content": article_obj.content,
        "article_querySet": article_querySet
    }
    HTML_STRING = render_to_string('home.html', context=context)
    return HttpResponse(HTML_STRING)
