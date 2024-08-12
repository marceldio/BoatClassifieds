from django.urls import include, path

from boat.apps import BoatConfig
from boat.views import BoatListView, BoatDetailView, BoatCreateView

app_name = BoatConfig.name

urlpatterns = [
    path('', BoatListView.as_view(), name='boat_list'),
    path('<int:pk>/', BoatDetailView.as_view(), name='boat_view'),
    path('offer/', BoatCreateView.as_view(), name='boat_create'),
]