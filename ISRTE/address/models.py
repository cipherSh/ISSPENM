from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название страны')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя области')
    city = models.BooleanField(verbose_name="Город")

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

    def __str__(self):
        return self.name


class District(models.Model):
    region_id = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Имя района')

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.name


class City(models.Model):
    district_id = models.ForeignKey(District, verbose_name='Район', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Имя города')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Village(models.Model):
    district_id = models.ForeignKey(District, verbose_name='Район', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Село')

    class Meta:
        verbose_name = 'Село'
        verbose_name_plural = 'Села'

    def __str__(self):
        return self.name



