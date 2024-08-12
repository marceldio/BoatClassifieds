from django.urls import path

from offer.apps import OfferConfig
from offer.views import OfferCreateView

app_name = OfferConfig.name

urlpatterns = [
    path('offer/', OfferCreateView.as_view(), name='offer'),
    ]
