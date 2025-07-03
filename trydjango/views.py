from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string


def home_view(request):

    object = Article.objects.get(id=1)
    article_qs = Article.objects.all()
    context = {
        'my_list': article_qs,
        'id': object.id,
        'title': object.title,
        'content': object.content
    }
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)