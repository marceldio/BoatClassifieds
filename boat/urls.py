from django.urls import include, path

import boat
from boat.apps import BoatConfig
from boat.views import BoatListView, BoatDetailView, BoatCreateView, BoatUpdateView, BoatDeleteView, contact

app_name = BoatConfig.name

urlpatterns = [
    path('', BoatListView.as_view(), name='boat_list'),
    path('<int:pk>/', BoatDetailView.as_view(), name='view_boat'),
    path('<int:pk>/delete/', BoatDeleteView.as_view(), name='delete_boat'),

    path('create/', BoatCreateView.as_view(), name='create_boat'),  # Для создания батареи с версиями
    path('<int:pk>/update/', BoatUpdateView.as_view(), name='update_boat'),

    path('contact/', contact, name='contact'),
]