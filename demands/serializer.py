from rest_framework import serializers

from demands.models import Demand


class DemandSerializer(serializers.ModelSerializer):
    """docstring for DemandSerializer."""

    class Meta:
        model = Demand
        exclude = ['created_at', 'updated_at']
        read_only_field = ['created', 'updated']
