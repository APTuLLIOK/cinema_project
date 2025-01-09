from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Movie, Session, Ticket
from .forms import TicketForm
from django.views.generic import TemplateView


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

    paginator = Paginator(sessions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    template = 'cinema/session/list.html'
    return render(request, template, context)


def session_detail(request, session_id):
    session = get_object_or_404(
        Session,
        id=session_id
    )
    available_seats = session.seats_for_session.prefetch_related('seat') \
        .filter(is_taken=False)

    template = 'cinema/session/detail.html'
    context = {
        'session': session,
        'seats_for_session': available_seats,
    }
    return render(request, template, context)


class ProfileView(TemplateView):
    template_name = 'cinema/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['username']
        user = get_object_or_404(get_user_model(), username=username)

        tickets = user.tickets.select_related('seat_for_session')
        paginator = Paginator(tickets, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'profile': user,
            'page_obj': page_obj
        }
        return context


@login_required
def tickets(request, session_id):
    session = get_object_or_404(
        Session,
        id=session_id
    )
    form = TicketForm(session_ID=session_id)
    template = 'cinema/tickets.html'
    context = {
        'session': session,
        'form': form
    }
    return render(request, template, context)


@login_required
def buy_ticket(request, session_id):
    form = TicketForm(request.POST, session_ID=session_id)
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.customer = request.user
        ticket.save()
    return redirect('cinema:profile', request.user.username)
