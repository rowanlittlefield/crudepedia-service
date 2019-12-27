import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from api.article.models import *

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article

class Query(ObjectType):
    article = graphene.Field(ArticleType, id=graphene.Int())
    articles = graphene.List(ArticleType)
    most_viewed = graphene.List(ArticleType)

    def resolve_article(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Article.objects.get(pk=id)

        return None

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

    def resolve_most_viewed(self, info, **kwargs):
        return Article.objects.all().order_by('-views')[0:5]

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
