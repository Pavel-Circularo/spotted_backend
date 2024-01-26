from rest_framework import viewsets, permissions
from .models import Brand, Car
from .serializers import BrandSerializer, CarSerializer


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer

    def get_queryset(self):
        # Only return cars that belong to the current user
        return Car.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
