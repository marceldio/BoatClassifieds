from django.urls import include, path

import boat
from boat.apps import BoatConfig
from boat.views import BoatListView, BoatDetailView, BoatCreateView, BoatUpdateView, BoatDeleteView, contact

app_name = BoatConfig.name

urlpatterns = [
    path('', BoatListView.as_view(), name='boat_list'),
    path('<int:pk>/', BoatDetailView.as_view(), name='boat_view'),
    path('<int:pk>/update/', BoatUpdateView.as_view(), name='boat_update'),
    path('<int:pk>/delete/', BoatDeleteView.as_view(), name='boat_delete'),
    path('create/', BoatCreateView.as_view(), name='boat_create'),  # Для создания батареи с версиями
    path('offer/', BoatCreateView.as_view(), name='boat_create'),
    path('contact/', contact, name='contact'),
]