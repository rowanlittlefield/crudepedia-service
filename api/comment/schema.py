import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django.utils import timezone
from api.comment.models import *
from api.comment.inputs import CommentCreateInput
from api.user.schema import UserType


class CommentType(DjangoObjectType):
    class Meta:
      model = Comment

class Query(ObjectType):
    comment = graphene.Field(CommentType, id=graphene.Int())
    comments = graphene.List(CommentType)

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Comment.objects.get(pk=id)

        return None

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()


class CreateComment(graphene.Mutation):
    class Arguments:
        data = CommentCreateInput(required=True)

    comment = graphene.Field(CommentType)

    @staticmethod
    def mutate(root, info, **kwargs):
        data = kwargs.pop('data')
        article = Article.objects.get(pk=data.get('article_id'))
        user = User.objects.get(pk=data.get('author_id'))
        comment = Comment(article=article,author=user,
                          body=data.get('body'), pub_date=timezone.now())
        
        comment.save()
        info.context.comments_by_article_id_loader.clear(article.id)
        return CreateComment(comment=comment)

class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()
