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
    list_display = ('movie', 'hall', 'datetime')
    list_filter = ('movie', 'hall', 'datetime')

    inlines = (
        SeatForSessionInline,
    )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    readonly_fields = ('session', 'customer')

    list_display = ('session', 'seat_for_session', 'customer', 'sold')
    list_editable = ('seat_for_session', 'sold')

    @admin.display(description='Session')
    def session(self, obj):
        return obj.seat_for_session.session
