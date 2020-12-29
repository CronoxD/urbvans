
# Django REST Framework
from rest_framework import serializers

# Models
from vans.models import Van


class VanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Van
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'uuid')
