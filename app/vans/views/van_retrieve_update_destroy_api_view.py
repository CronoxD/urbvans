
# Django REST Framework
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Serializers
from vans.serializers import VanSerializer

# Models
from vans.models import Van


class VanRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint retrieve a van detail with their uuid.
    You can destroy (DELETE method ) and update (PUT and PATCH method)
    """
    queryset = Van.objects.all()
    serializer_class = VanSerializer
    lookup_field = 'uuid'