from django.utils.functional import cached_property
from api.comment.loaders import CommentsByArticleIdLoader


class GQLContext:
    @cached_property
    def comments_by_article_id_loader(self):
        return CommentsByArticleIdLoader()
