from rest_framework import serializers
from .models import Brand, Car


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'color', 'year', 'picture']

    def create(self, validated_data):
        # If there's an image, handle the image file separately
        picture = validated_data.pop('picture', None)
        user = validated_data.pop('user', None)
        car = Car.objects.create(**validated_data, user=user)

        if picture is not None:
            car.picture.save(picture.name, picture, save=True)

        return car
