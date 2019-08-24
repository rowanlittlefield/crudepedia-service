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

class ViewArticle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()
    article = graphene.Field(ArticleType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        article_instance = Article.objects.get(pk=id)
        if article_instance:
            ok = True
            article_instance.views += 1
            article_instance.save()
            return ViewArticle(ok=ok, article=article_instance)
        return ViewArticle(ok=ok, article=None)


class Mutation(graphene.ObjectType):
    view_article = ViewArticle.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
