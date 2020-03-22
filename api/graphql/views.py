import os
from importlib import import_module
import graphene
from django.utils.functional import cached_property
from graphene_django.views import GraphQLView


packages = [name for name in os.listdir('./api') if
            os.path.isdir(f'./api/{name}')
            and name[0] != '_'
            and os.path.exists(f'./api/{name}/context.py')]

context_classes = []
for package in packages:
    module = import_module(f'api.{package}.context')
    if hasattr(module, 'GQLContext'):
        context_classes.append(module.GQLContext)

class GQLContext(*context_classes):
    def __init__(self, request):
        self.request = request

    @cached_property
    def user(self):
        return self.request.user

class CustomGraphQLView(GraphQLView):
    def get_context(self, request):
        return GQLContext(request)
