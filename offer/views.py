from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from boat.models import Boat
from boat.views import BoatCreateView, BoatUpdateView

from order.services import send_order_email


class OfferCreateView(BoatUpdateView):
    model = Boat
    fields = ('name', 'year', 'description', 'image', 'price', 'owner')
    success_url = reverse_lazy('boat:boat_list')
    template_name = 'boat/boat_form.html'

    def get_success_url(self):
        return reverse('boat:boat_detail', kwargs={'pk': self.object.pk})

