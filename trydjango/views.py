from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string


def home_view(request):

    object = Article.objectects.get(id=1)
    context = {
        'id': object.id,
        'title': object.title,
        'content': object.content
    }
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)