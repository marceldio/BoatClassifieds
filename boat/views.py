from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from boat.forms import BoatForm, VersionForm
from boat.models import Boat, Version


class BoatCreateView(CreateView):
    model = Boat
    form_class = BoatForm
    success_url = reverse_lazy('boat:boat_list')
    template_name = 'boat/boat_form.html'


class BoatUpdateView(UpdateView):
    model = Boat
    form_class = BoatForm
    # success_url = reverse_lazy('boat:boat_list')

    def get_success_url(self):
        # return reverse('boat:boat_view', kwargs={'pk': self.object.pk})
        return reverse('boat:boat_view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Boat, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


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



