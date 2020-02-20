import graphene
import sensors.schema


class Query(sensors.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
