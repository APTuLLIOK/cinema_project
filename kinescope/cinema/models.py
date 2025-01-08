from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from datetime import datetime as dt


User = get_user_model()


class Genre(models.Model):
    title = models.CharField(
        unique=True,
        max_length=128,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title


class Hall(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Название/номер'
    )
    seats_quantity = models.IntegerField(
        validators=[MinValueValidator(10)],
        verbose_name='Количество мест',
        help_text='Мест должно быть не менее 10'
    )

    class Meta:
        verbose_name = 'зал'
        verbose_name_plural = 'Залы'

    def __str__(self):
        return self.title


class Seat(models.Model):
    number = models.CharField(
        max_length=10,
        verbose_name='Номер'
    )
    hall = models.ForeignKey(
        Hall,
        on_delete=models.CASCADE,
        related_name='seats',
        verbose_name='Зал'
    )

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return f'{self.hall.title}-{self.number}'


class Movie(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Название'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.RESTRICT,
        related_name='movies',
        verbose_name='Жанр'
    )
    duration = models.TimeField(
        verbose_name='Продолжительность',
        default='01:00'
    )
    description = models.CharField(
        max_length=512,
        verbose_name='Описание'
    )
    poster = models.ImageField(
        upload_to='posters',
        verbose_name='Постер'
    )
    is_in_the_cinema = models.BooleanField(
        verbose_name='В прокате',
        default=True
    )

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class Session(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='sessions',
        verbose_name='Фильм'
    )
    hall = models.ForeignKey(
        Hall,
        on_delete=models.CASCADE,
        related_name='sessions',
        verbose_name='Зал'
    )
    datetime = models.DateTimeField(
        verbose_name='Дата и время'
    )
    seats = models.ManyToManyField(
        Seat,
        through='SeatForSession'
    )

    class Meta:
        verbose_name = 'сеанс'
        verbose_name_plural = 'Сеансы'
        ordering = ('datetime',)

    def __str__(self):
        return self.movie.title + ' - ' \
              + self.datetime.strftime('%d.%m.%Y %H:%M')


class SeatForSession(models.Model):
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='seats_for_session',
        verbose_name='Сеанс'
    )
    seat = models.ForeignKey(
        Seat,
        on_delete=models.CASCADE,
        related_name='sessions',
        verbose_name='Место'
    )
    is_taken = models.BooleanField(
        verbose_name='Занято'
    )

    class Meta:
        verbose_name = 'место на сеанс'
        verbose_name_plural = 'Места на сеанс'

    def __str__(self):
        return f'{self.session.__str__()} - {self.seat.__str__()}'


class Ticket(models.Model):
    seat_for_session = models.ForeignKey(
        SeatForSession,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name='Место на сеанс'
    )
    customer = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='tickets',
        verbose_name='Покупатель'
    )

    class Meta:
        verbose_name = 'билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return (self.seat_for_session.__str__()
                + ' - ' + self.customer.username)
