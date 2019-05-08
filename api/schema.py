import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from api.articles.models import *

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article

class Query(ObjectType):
    article = graphene.Field(ArticleType, id=graphene.Int())
    articles = graphene.List(ArticleType)

    def resolve_article(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Article.objects.get(pk=id)

        return None

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

schema = graphene.Schema(query=Query)
