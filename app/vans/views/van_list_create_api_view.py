
# Django
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

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

    # Cache page for the requested url
    # Cache timeout 1 hour
    @method_decorator(cache_page(60*60))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
