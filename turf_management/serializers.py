
from rest_framework import serializers

from turf_management.models import Turf

class TurfSerializer(serializers.Serializer):

    id=serializers.IntegerField(read_only=True) # for viewing only, no need to pass

    name = serializers.CharField()

    location = serializers.CharField()

    address = serializers.CharField()

    description = serializers.CharField()   

    opening_time = serializers.TimeField()

    closing_time = serializers.TimeField()

    day_price = serializers.DecimalField(
    max_digits=8,
    decimal_places=2
    )

    night_price = serializers.DecimalField(
    max_digits=8,
    decimal_places=2
    )

    facilities = serializers.CharField()


    # create() method --> POST()
    def create(self, validated_data):
        return Turf.objects.create(**validated_data)

    # Update () method --> PUT()

    def update(self, instance, validated_data):
       # return Turf.objects.filter(id=instance.id).update(** validated_data)
       for attribute,values in validated_data.items():
           setattr(instance,attribute,values)
           instance.save()
       return instance



