from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer

def article_list(request):
    # get all the articles
    articles = Article.objects.all()
    # serialize them
    serializer =  ArticleSerializer(articles, many=True)
    # return JSON
    return JsonResponse({'articles': serializer.data}, safe=False)

