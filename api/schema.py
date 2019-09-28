import os
from importlib import import_module
import graphene

packages = [name for name in os.listdir('./api') if
            os.path.isdir(f'./api/{name}')
            and name[0] != '_'
            and os.path.exists(f'./api/{name}/schema.py')]

query_classes = []
mutation_classes = []
for package in packages:
    module = import_module(f'api.{package}.schema')
    if hasattr(module, 'Query'):
        query_classes.append(module.Query)
    if hasattr(module, 'Mutation'):
        mutation_classes.append(module.Mutation)

query = type('Query', (*query_classes, graphene.ObjectType), {})
mutation = type('Mutation', (*mutation_classes, graphene.ObjectType), {})

schema = graphene.Schema(query=query, mutation=mutation)
