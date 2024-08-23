from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from boat.forms import BoatForm, VersionForm, BoatModeratorForm
from boat.models import Boat, Version

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'boat/contact.html')


class BoatCreateView(LoginRequiredMixin, CreateView):
    model = Boat
    form_class = BoatForm
    success_url = reverse_lazy('boat:boat_list')
    template_name = 'boat/boat_form.html'

    def form_valid(self, form):
        boat = form.save()
        user = self.request.user
        boat.owner = user
        boat.save()

        return super().form_valid(form)


class BoatUpdateView(LoginRequiredMixin, UpdateView):
    model = Boat
    form_class = BoatForm
    template_name = ('boat/boat_form.html')

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
        context_data = self.get_context_data()
        formset = context_data['formset']
        # self.object = form.save()
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner or user.has_perm('boat.change_boat'):
            return BoatForm

        if user.has_perm('boat.can_edit_description') and user.has_perm('boat.can_edit_is_published'):
            return BoatModeratorForm

        raise PermissionDenied

class BoatDeleteView(DeleteView):
    model = Boat
    success_url = reverse_lazy('boat:boat_list')
    template_name = 'boat/boat_delete.html'

    def get_success_url(self):
        return reverse('boat:boat_list')



class BoatListView(ListView):
    model = Boat
    template_name = ('boat/boat_list.html')
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        boats = self.get_queryset()
        for boat in boats:
            boat.version = boat.version_set.filter(is_current=True).first()

        context_data['object_list'] = boats
        return context_data


class BoatDetailView(DetailView):
    model = Boat

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object
