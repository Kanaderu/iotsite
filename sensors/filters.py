from rest_framework.filters import BaseFilterBackend
import coreapi


class NameFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='name',
            location='query',
            required=False,
            type='string',
            description='name of recording'
        )]

    def filter_queryset(self, request, queryset, view):
        try:
            n = request.query_params['name']
            queryset = queryset.filter(name=n)
        except KeyError:
            # no query parameters
            pass
        return queryset