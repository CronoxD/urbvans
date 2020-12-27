
# Django REST Framework
from rest_framework import serializers

# Models
from vans.models import Van


class VanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Van
        fields = '__all__'
