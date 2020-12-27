
# Django
from django.urls import path

# View
from vans import views


app_name = 'vans'


urlpatterns = [
    path('vans/', views.VanListCreateAPIView.as_view(), name='van-list'),
    path('vans/<uuid>/', views.VanRetrieveUpdateDestroyAPIView.as_view(), name='van-detail'),
]
