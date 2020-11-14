from django.contrib import admin
from . models import Flight,Airport,Passenger,Airways

class PassengerInline(admin.StackedInline):
    model =  Passenger.flight.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flight",)
    list_display = ("first_name","last_name")

admin.site.register(Flight , FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger ,PassengerAdmin)
admin.site.register(Airways)