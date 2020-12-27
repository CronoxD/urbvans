
# Django REST Framework
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Serializers
from vans.serializers import VanSerializer

# Models
from vans.models import Van


class VanRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Van.objects.all()
    serializer_class = VanSerializer
    lookup_field = 'uuid'