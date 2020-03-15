from collections import defaultdict
from promise import Promise
from promise.dataloader import DataLoader
# from blog.models import Comment
from django.contrib.auth.models import User


class AuthorsByArticleIdLoader(DataLoader):
    def batch_load_fn(self, article_ids):
        authors_by_article_ids = {}

        for idx, author in enumerate(User.objects.filter(article__in=article_ids).iterator()):
            article_id = article_ids[idx]
            authors_by_article_ids[article_id] = author

        return Promise.resolve([authors_by_article_ids.get(article_id)
                                for article_id in article_ids])
