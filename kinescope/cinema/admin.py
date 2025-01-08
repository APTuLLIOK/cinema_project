from django.contrib import admin
from .models import Genre, Movie, Hall, Seat, Session, SeatForSession, Ticket


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    pass


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    pass


class SeatForSessionInline(admin.StackedInline):
    model = SeatForSession
    extra = 0


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    inlines = (
        SeatForSessionInline,
    )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
