from collections import defaultdict
from promise import Promise
from promise.dataloader import DataLoader
from django.contrib.auth.models import User
from api.comment.models import Comment


class AuthorsByArticleIdLoader(DataLoader):
    def batch_load_fn(self, article_ids):
        authors_by_article_ids = {}

        for idx, author in enumerate(User.objects.filter(article__in=article_ids).iterator()):
            article_id = article_ids[idx]
            authors_by_article_ids[article_id] = author

        return Promise.resolve([authors_by_article_ids.get(article_id)
                                for article_id in article_ids])

class CommentsByArticleIdLoader(DataLoader):
    def batch_load_fn(self, article_ids):
        comments_by_article_ids = defaultdict(list)

        for comment in Comment.objects.filter(article_id__in=article_ids).iterator():
            comments_by_article_ids[comment.article_id].append(comment)

        return Promise.resolve([comments_by_article_ids.get(article_id, [])
                                for article_id in article_ids])
