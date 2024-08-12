from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from boat.forms import BoatForm
from boat.models import Boat

class BoatCreateView(CreateView):
    model = Boat
    form_class = BoatForm
    success_url = reverse_lazy('boat:boat_list')
    template_name = 'boat/boat_create.html'


class BoatUpdateView(UpdateView):
    model = Boat
    form_class = BoatForm
    success_url = reverse_lazy('boat:boat_list')

    def get_success_url(self):
        # return reverse('boat:boat_detail', kwargs={'pk': self.object.pk})
        return reverse('boat:boat_list', args=[self.kwargs.get('pk')])


class BoatDeleteView(DeleteView):
    model = Boat
    success_url = reverse_lazy('boat:boat_list')
    template_name = 'boat/boat_delete.html'

    def get_success_url(self):
        return reverse('boat:boat_list')



class BoatListView(ListView):
    model = Boat


class BoatDetailView(DetailView):
    model = Boat

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object



