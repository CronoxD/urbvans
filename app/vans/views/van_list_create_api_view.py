
# Django REST Framework
from rest_framework.generics import ListCreateAPIView

# Models
from vans.models import Van

# Serializers
from vans.serializers import VanSerializer


class VanListCreateAPIView(ListCreateAPIView):
    queryset = Van.objects.all()
    serializer_class = VanSerializer
    filterset_fields = ['status']
