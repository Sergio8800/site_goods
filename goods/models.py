from time import time

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class CarName(models.Model):
    """Название Компании производителя машин"""
    name = models.CharField("Name", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car label"
        verbose_name_plural = "Cars label"
class Genre(models.Model):
    """Марка"""
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"
class Specifications(models.Model):
    """Характеристики"""

    fuel_type = models.CharField("Тип топлива", max_length=100)


    def __str__(self):
        return self.fuel_type

    class Meta:
        verbose_name = "Топливо"
        verbose_name_plural = "Топливо"

class Category(models.Model):
    """Категории"""
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))
class Car(models.Model):
    """Фильм"""
    title = models.ForeignKey(CarName, verbose_name="Cars", on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre,  max_length=100)
    category = models.ManyToManyField(Category,  max_length=100)
    fuel = models.ManyToManyField(Specifications,  max_length=100)
    poster = models.ImageField("Фото", default=None, upload_to="movies/")
    price = models.PositiveIntegerField("Цена", default=0, help_text="указывать сумму в долларах")
    slug = models.SlugField("Url", max_length=150, blank=True, unique=False)

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title.name

    def get_absolute_url(self):
        return reverse("car_detail_url", kwargs={"slug": self.slug})


    # def get_review(self):
    #     return self.reviews_set.filter(parent__isnull=True)


    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

class CarShorts(models.Model):
    image = models.ImageField("Pictures", upload_to="movie_shots/")
    car = models.ForeignKey(Car, verbose_name="Car", on_delete=models.CASCADE)

    def __str__(self):
        return self.car.title.name
    class Meta:
        verbose_name = "Short"
        verbose_name_plural = "Shorts"

class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    # ip = models.CharField("IP адрес", max_length=15, default=None)
    email = models.EmailField(default='test@gmail.com')
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="машина")

    def __str__(self):
        return f"{self.star} - {self.car}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    date_post = models.DateTimeField("Дата сообщения")
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    car = models.ForeignKey(Car, verbose_name="Car", on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} - {self.car}"



    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-date_post']


