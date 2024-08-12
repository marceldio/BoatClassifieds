from django.forms import ModelForm

from boat.models import Boat


class BoatForm(ModelForm):
    class Meta:
        model = Boat
        fields = "__all__"