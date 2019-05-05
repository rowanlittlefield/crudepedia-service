from django.http import JsonResponse
from .models import Article

def index(request):
    response = { 'articles': [] }
    article_list = Article.objects.all()
    for article in article_list:
        response['articles'].append({
        'id': article.id,
        'title': article.title,
        })

    return JsonResponse(response)

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    response = {
    'id': article.id,
    'title': article.title,
    'pub_date': article.pub_date,
    'introduction': article.introduction,
    'description': article.description,
    'views': article.views,
    }
    return JsonResponse(response)
