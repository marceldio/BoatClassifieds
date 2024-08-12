from django.contrib import admin

from boat.models import Owner, Boat, BoatHistory, Version


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'image', 'price', 'owner')
    list_filter = ('owner', 'year', 'price',)
    search_fields = ('name', 'year', 'price',)


@admin.register(BoatHistory)
class BoatHistory(admin.ModelAdmin):
    list_display = ('boat', 'start_year', 'stop_year', 'owner',)
    list_filter = ('owner', 'boat',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('title', 'boat')
    list_filter = ('boat',)
    search_fields = ('boat', 'version')
