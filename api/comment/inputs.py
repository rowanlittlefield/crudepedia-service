from graphene import InputObjectType, ID, String


class CommentCreateInput(InputObjectType):
    article_id = ID(required=True)
    author_id = ID(required=True)
    body = String(required=True)
