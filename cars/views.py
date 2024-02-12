from rest_framework import viewsets, permissions
from .models import Brand, Car
from .serializers import BrandSerializer, CarSerializer
from .filters import CarFilter


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    filterset_class = CarFilter

    def get_queryset(self):
        queryset = Car.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
