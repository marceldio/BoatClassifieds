from django.contrib import admin

from offer.models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('boat', 'owner',)
    list_filter = ('boat', 'owner')
