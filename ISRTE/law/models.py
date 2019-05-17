from django.db import models
from django.shortcuts import reverse
from persons.models import Criminals


# Create your models here.


class CriminalCase(models.Model):
    number = models.CharField(max_length=200, verbose_name='Номер уголовного дела')
    year = models.CharField(max_length=10, verbose_name='Год уголовного дела')
    article = models.CharField(max_length=200, verbose_name='Уголовный кодекс - Статья')
    organ = models.CharField(max_length=200, verbose_name='Возбудивший орган')
    date_arousal = models.DateField(null=True, blank=True, verbose_name='Дата возбуждение')
    date_suspension = models.DateField(null=True, blank=True, verbose_name='Дата приостановления')
    remarks = models.TextField(null=True, blank=True, verbose_name="Примечание")

    class Meta:
        verbose_name = 'Уголовное дело'
        verbose_name_plural = 'Уголовные дела'
        ordering = ["year", "number"]

    def __str__(self):
        return self.number + '/' + self.year


class CriminalCaseCriminals(models.Model):
    criminal_case = models.ForeignKey(CriminalCase, verbose_name='Уголовное дело', on_delete=models.CASCADE)
    criminal_id = models.ForeignKey(Criminals, verbose_name='Люди проходящие по делу', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Уголовное дело -- ответчики'
        verbose_name_plural = 'Уголовное дело -- ответчики'

    def __str__(self):
        return CriminalCase.__str__() + ' -- ' + Criminals.__str__()


class Manhunt(models.Model):
    criminal_id = models.ForeignKey(Criminals, verbose_name='Человек в розыске', on_delete=models.PROTECT)
    invest_case_number = models.CharField(max_length=200, verbose_name='Номер розыскного дело')
    criminalCase_id = models.ForeignKey(CriminalCase, verbose_name='Номмер уголовного дело', on_delete=models.PROTECT)
    date_arousal = models.DateField(verbose_name='Дата заведения розыскного дела')
    invest_initiator = models.CharField(max_length=200, verbose_name='Инициатор заведивщий дело')
    invest_category = models.CharField(null=True, blank=True, max_length=200, verbose_name='Категория учета розыска')
    circular_number = models.CharField(null=True, blank=True, max_length=200, verbose_name='Номер циркуляра')
    preventive = models.CharField(max_length=200, verbose_name='Мера пресечения')
    date_inter_invest = models.DateField(null=True, blank=True, verbose_name='Дата поступления в международный розыск')
    invest_stopped = models.BooleanField(verbose_name='Розыск прекращен')
    place_detention = models.CharField(max_length=200, null=True, blank=True, verbose_name='Место задержания')
    date_detention = models.DateField(null=True, blank=True, verbose_name='Дата задержания')
    invest_stopped_circular = models.CharField(max_length=200, null=True, blank=True,
                                               verbose_name='Номер циркуляра о прекращении розыска')

    class Meta:
        verbose_name = 'Розыскное дело'
        verbose_name_plural = 'Розыскные дела'
        ordering = ["criminal_id"]

    def __str__(self):
        return self.invest_case_number


class Conviction(models.Model):
    criminal_id = models.ForeignKey(Criminals, verbose_name='ФИО', on_delete=models.PROTECT)
    criminal_case_number = models.CharField(max_length=200, verbose_name='Номер уголовного дело', null=True)
    criminal_case_year = models.CharField(max_length=10, verbose_name='Год уголовного дело')
    criminal_case_organ = models.CharField(max_length=200, verbose_name='Орган возбудивщий угоовного дело')
    law_article = models.CharField(max_length=200, verbose_name='Статья УК')
    date_sentence = models.DateField(verbose_name='Дата приговора')
    date_release = models.DateField(verbose_name='Дата освобождения')

    class Meta:
        verbose_name = 'Судимость'
        verbose_name_plural = 'Судимости'
        ordering = ["criminal_id"]

    def __str__(self):
        return self.criminal_case_number + '/' + self.criminal_case_year + ' --- ' + str(self.date_sentence)


class Confluence(models.Model):
    criminal_id = models.ForeignKey(Criminals, verbose_name='ФИО', on_delete=models.PROTECT)
    PRES_CHOICES = (
        ('V', 'Выезд'),
        ('Z', 'Въезд')
    )
    pres = models.CharField(max_length=1, choices=PRES_CHOICES, default='V', verbose_name='Выезд/въезд')
    kind = models.CharField(max_length=200, verbose_name='Вид пересечение')
    date = models.DateField(null=True, blank=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Пересечение'
        verbose_name_plural = 'Таблица пересечений'
        ordering = ["criminal_id"]

    def __str__(self):
        return self.criminal_id + '--' + self.pres + '--' + self.date
