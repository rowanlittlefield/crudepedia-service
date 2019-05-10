import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from api.articles.models import *
from django.contrib.auth.models import User

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(ObjectType):
    article = graphene.Field(ArticleType, id=graphene.Int())
    user = graphene.Field(UserType, id=graphene.Int())
    articles = graphene.List(ArticleType)
    users = graphene.List(UserType)

    def resolve_article(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Article.objects.get(pk=id)

        return None

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return User.objects.get(pk=id)

        return None

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()
    
    def resolve_users(self, info, **kwargs):
        return User.objects.all()

schema = graphene.Schema(query=Query)
