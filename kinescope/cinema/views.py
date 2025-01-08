from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Movie, Session, SeatForSession


def index(request):
    template = 'cinema/index.html'
    movies = Movie.objects.select_related('genre') \
        .filter(is_in_the_cinema=True)
    context = {
        'movies': movies,
    }
    return render(request, template, context)


def movie_detail(request, movie_id):
    current_time = timezone.now()
    movie = get_object_or_404(
        Movie,
        id=movie_id,
        is_in_the_cinema=True
    )

    sessions = movie.sessions.all().filter(
        datetime__gte=current_time
    )

    template = 'cinema/detail.html'
    context = {
        'movie': movie,
        'sessions': sessions
    }
    return render(request, template, context)


def session_list(request):
    current_time = timezone.now()
    sessions = Session.objects.all().filter(
        datetime__gte=current_time
    )

    context = {
        'sessions': sessions
    }
    template = 'cinema/session/list.html'
    return render(request, template, context)


def session_detail(request, session_id):
    session = get_object_or_404(
        Session,
        id=session_id
    )
    available_seats = session.seats_for_session.select_related('seat').filter(
        is_taken=False
    )

    template = 'cinema/session/detail.html'
    context = {
        'session': session,
        'seats_for_session': available_seats,
    }
    return render(request, template, context)
