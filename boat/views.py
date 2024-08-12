from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from boat.models import Boat

class BoatCreateView(CreateView):
    model = Boat
    fields = ('name', 'year', 'description', 'image', 'price', 'owner')
    success_url = reverse_lazy('boat:boat_list')
    template_name = 'boat/boat_create.html'


class BoatUpdateView(UpdateView):
    model = Boat
    fields = ('name', 'year', 'description', 'image', 'price', 'owner')
    success_url = reverse_lazy('boat:boat_list')

    def get_success_url(self):
        return reverse('boat:boat_detail', kwargs={'pk': self.object.pk})

class BoatListView(ListView):
    model = Boat


class BoatDetailView(DetailView):
    model = Boat




