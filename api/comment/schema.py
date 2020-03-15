import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from api.comment.models import *
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
