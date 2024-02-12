import django_filters
from .models import Car


class CarFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name='brand__name')

    class Meta:
        model = Car
        fields = ['user', 'brand', 'model', 'color', 'year']
