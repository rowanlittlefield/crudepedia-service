from django.utils.functional import cached_property
from api.user.loaders import AuthorsByArticleIdLoader


class GQLContext:
    @cached_property
    def authors_by_article_id_loader(self):
        return AuthorsByArticleIdLoader()
