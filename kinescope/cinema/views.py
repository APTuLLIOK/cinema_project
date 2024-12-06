from django.shortcuts import render
from django.http import Http404


movies = [
    {
        'id': 0,
        'title': 'Фильм №1',
        'genre': 'Жанр 1',
        'description': 'Зольтрак — это базовое атакующее заклинание в мире аниме «Атака на титанов». Оно выглядит как белый светящийся луч и изначально было создано демоном Квалем. Однако благодаря Фрирен это заклинание было проанализировано и переработано, став основой для человеческой школы магии.',
        'sessions': [0],
    },
    {
        'id': 1,
        'title': 'Фильм №2',
        'genre': 'Жанр 1',
        'description': '«Загадочный мир: путешествие в неизведанное» — это захватывающий фильм, который отправит вас в удивительное приключение по неизведанным уголкам нашей планеты. В центре сюжета — группа исследователей, которые отправляются в экспедицию, чтобы раскрыть тайны древних цивилизаций и найти затерянные сокровища.',
        'sessions': [],
    },
    {
        'id': 2,
        'title': 'Фильм №3',
        'genre': 'Жанр 2',
        'description': 'Очередное описание, написанное с помощью ИИ',
        'sessions': [1],
    },
    {
        'id': 3,
        'title': 'Фильм №4',
        'genre': 'Жанр 2',
        'description': 'Нет слов',
        'sessions': [2, 3],
    },
]

sessions = [
    {
        'id': 0,
        'datetime': '01.01.2001 14:00',
        'movie_id': 0,
        'seats': [1, 2, 3],
    },
    {
        'id': 1,
        'datetime': '01.01.2001 15:00',
        'movie_id': 2,
        'seats': [1, 2, 3],
    },
    {
        'id': 2,
        'datetime': '02.01.2001 10:00',
        'movie_id': 3,
        'seats': [1, 2, 3],
    },
    {
        'id': 3,
        'datetime': '02.01.2001 12:00',
        'movie_id': 3,
        'seats': [1, 2, 3],
    },
]

movie_ids = {movie['id']: movie for movie in movies}
session_ids = {session['id']: session for session in sessions}


def index(request):
    template = 'cinema/index.html'
    context = {
        'movies': movies,
    }
    return render(request, template, context)


def movie_detail(request, movie_id):
    movie = movie_ids.get(movie_id)
    if not movie:
        raise Http404(f'Фильм с ID {movie_id} не найден.')

    template = 'cinema/detail.html'
    context = {
        'movie': movie,
    }
    return render(request, template, context)


def session_list(request, date):
    template = 'cinema/session/list.html'
    context = {
        'date': date,
    }
    return render(request, template, context)


def session_detail(request, session_id):
    session = session_ids.get(session_id)
    if not session:
        raise Http404(f'Сеанс с ID {session_id} не найден.')

    template = 'cinema/session/detail.html'
    context = {
        'session': session,
    }
    return render(request, template, context)
