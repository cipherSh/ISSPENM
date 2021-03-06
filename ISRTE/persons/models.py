from django.db import models
from django.urls import reverse

# Create your models here.
from address.models import Country, Region, District, City, Village
from users.models import Profile, TrustLevel


class Occupation(models.Model):
    type_occ = models.CharField(max_length=40, verbose_name='Тип деятельности')
    occ_abbr = models.CharField(max_length=40, verbose_name='Аббревиатура')
    remarks = models.TextField(verbose_name='Примечание')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип деятельности'

    def __str__(self):
        return self.occ_abbr


class Organizations(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название организации')
    occupation = models.ForeignKey(Occupation, null=True, blank=True, verbose_name='Тип организации',
                                   on_delete=models.SET_NULL)
    leader = models.CharField(max_length=200, null=True, blank=True, verbose_name='Лидер организации')
    ideology = models.CharField(max_length=200, null=True, blank=True, verbose_name='Идеология организации')
    foundation_year = models.CharField(max_length=20, null=True, blank=True, default='Неизвестно',
                                       verbose_name='Год основание')
    remarks = models.TextField(blank=True, null=True, verbose_name='Примечание')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Запрещенные организации'
        ordering = ["name"]

    def __str__(self):
        return self.name


class RelativeRelation(models.Model):
    type = models.CharField(max_length=200, verbose_name='Вид связи')
    direct = models.CharField(max_length=200, verbose_name='Прямое')
    inverse = models.CharField(max_length=200, verbose_name='Обратное')

    class Meta:
        verbose_name = 'Вид связи'
        verbose_name_plural = 'Виды связей'
        ordering = ["type"]

    def __str__(self):
        return self.type


class ContactRelation(models.Model):
    type = models.CharField(max_length=200, verbose_name='Вид связи')
    direct = models.CharField(max_length=200, verbose_name='Прямое')
    inverse = models.CharField(max_length=200, verbose_name='Обратное')

    class Meta:
        verbose_name = 'Вид отношении'
        verbose_name_plural = 'Виды отношений'
        ordering = ["type"]

    def __str__(self):
        return self.type


class Criminals(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, blank=True, verbose_name='Отчетство')
    full_name = models.CharField(max_length=600, blank=True, null=True, default='',
                                 verbose_name='Полное имя')
    birthday = models.DateField(verbose_name='Дата рождение', auto_now_add=False, blank=True)
    birth_country = models.CharField(max_length=200, verbose_name='Страна рождения', null=True, blank=True)
    birth_region = models.CharField(max_length=200, verbose_name='Область', null=True, blank=True)
    birth_District = models.CharField(max_length=200, verbose_name='Район', null=True, blank=True)
    birth_City = models.CharField(max_length=200, verbose_name='Город', null=True, blank=True)
    birth_Village = models.CharField(max_length=200, verbose_name='Село', null=True, blank=True)
    GENDER_CHOICES = (
        ('N', 'Не указан'),
        ('M', 'Мужской'),
        ('F', 'Женский')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    citizenship = models.CharField(max_length=200, default='Не указан', verbose_name='Гражданство')
    INN = models.CharField(max_length=14, verbose_name='ПИН')
    passport_serial = models.CharField(max_length=2, verbose_name='Серия паспорта')
    passport_number = models.CharField(max_length=7, verbose_name='Номер паспорта')
    issue_organ = models.CharField(max_length=200, verbose_name='Место выдачи')
    issue_data = models.DateField(verbose_name='Дата выдачи', auto_now_add=False)
    EDUCATION_CHOICES = (
        ('NS', 'Не указан'),
        ('NOT', 'Нет образование'),
        ('PGE', 'Начальное общее образование'),
        ('BGE', 'Основное общее образование'),
        ('SGE', 'Среднее общее образование'),
        ('SVE', 'Среднее профессиональное образование'),
        ('HEB', 'Высшее образование - бакалавриат'),
        ('HES', 'Высшее образование - специалитет, магистратура'),
        ('HET', 'Высшее образование - подготовка кадров высшей квалификации')
    )
    education = models.CharField(max_length=3, choices=EDUCATION_CHOICES, default='NS', verbose_name='Образование')
    education_place = models.CharField(max_length=200, null=True, blank=True, verbose_name="Место образование")
    profession = models.CharField(max_length=200, default='Нет профессии', verbose_name='Профессия', null=True)
    MARITAL_CHOICES = (
        ('N', 'Не указан'),
        ('SB', 'Холост'),
        ('SG', 'Незамужем'),
        ('MB', 'Женат'),
        ('MG', 'Замужен'),
        ('D', 'Разведен(а)')
    )
    marital_status = models.CharField(max_length=2, choices=MARITAL_CHOICES, default='N', verbose_name='Семейное '
                                                                                                       'положение')
    occupation = models.ForeignKey(Occupation, verbose_name='Деятелльность', on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = (
        ('N', 'Неизвестно'),
        ('D', 'Мертв'),
        ('L', 'Жив')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="N", verbose_name='Статус')
    image = models.ImageField(null=True, blank=True, upload_to="images/criminals/",
                              verbose_name='Фото')
    organization = models.ForeignKey(Organizations, blank=True, verbose_name='Организации', on_delete=models.SET_NULL,
                                     null=True)
    remarks = models.TextField(blank=True, verbose_name='Примечание', null=True)
    user = models.ForeignKey(Profile, max_length=200, verbose_name='Создал', on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True, verbose_name='Дата создание')
    owner = models.ForeignKey(Profile, verbose_name='Владелец', related_name="Owner", on_delete=models.SET_NULL,
                              null=True)
    close = models.BooleanField(verbose_name="Закрыть доступ", default=False)
    confident = models.ForeignKey(TrustLevel, on_delete=models.PROTECT, null=True, blank=True,
                                  verbose_name="Уровень секретности")
    check = models.BooleanField(verbose_name='Подтверждение', default=False)

    class Meta:
        verbose_name = 'Террориста или экстремиста'
        verbose_name_plural = 'Террористы и экстремисти'
        ordering = ["last_name", "first_name", "patronymic"]

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic

    def get_absolute_url(self):
        return reverse('criminal_single_url', kwargs={'pk': self.id})

    def get_update_url(self):
        return reverse('criminal_update_url', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('criminal_delete_url', kwargs={'pk': self.id})

    def get_group_access_create_url(self):
        return reverse('group_access_create_url', kwargs={'pk': self.id})

    def get_personal_access_create_url(self):
        return reverse('personal_access_create_url', kwargs={'pk': self.id})

    def get_relative_add_url(self):
        return reverse('relative_add_url', kwargs={'pk': self.id})

    def get_contact_person_add_url(self):
        return reverse('contact_person_add_url', kwargs={'pk': self.id})

    def get_address_add_url(self):
        return reverse('address_add_url', kwargs={'pk': self.id})

    def get_contact_add_url(self):
        return reverse('contact-detail_add_url', kwargs={'pk': self.id})

    def get_conviction_add_url(self):
        return reverse('conviction_add_url', kwargs={'pk': self.id})

    def get_criminal_case_add_url(self):
        return reverse('criminal_case_add_url', kwargs={'pk': self.id})

    def get_manhunt_add_url(self):
        return reverse('manhunt_add_url', kwargs={'pk': self.id})

    def get_criminal_close_change_url(self):
        return reverse('criminal_close_change_url', kwargs={'pk': self.id})

    def get_criminal_check_url(self):
        return reverse('criminal_check_url', kwargs={'pk': self.id})

    def get_criminal_change_owner_url(self):
        return reverse('criminal_change_owner_url', kwargs={'pk': self.id})

    def get_criminal_confident_change_url(self):
        return reverse('criminal_confident_change_url', kwargs={'pk': self.id})


class Persons(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, verbose_name='Отчетство',  null=True, blank=True)
    birthday = models.DateField("Дата рождение", auto_now_add=False, null=True, blank=True)
    birth_country = models.CharField(max_length=200, verbose_name='Страна рождения', null=True, blank=True)
    birth_region = models.CharField(max_length=200, verbose_name='Область', null=True, blank=True)
    birth_District = models.CharField(max_length=200, verbose_name='Район', null=True, blank=True)
    birth_City = models.CharField(max_length=200, verbose_name='Город', null=True, blank=True)
    birth_Village = models.CharField(max_length=200, verbose_name='Село', null=True, blank=True)
    GENDER_CHOICES = (
        ('N', 'Не указан'),
        ('M', 'Мужской'),
        ('F', 'Женский')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    citizenship = models.CharField(max_length=200, default='Не указан', verbose_name='Гражданство',  null=True, blank=True)
    INN = models.CharField(max_length=14, verbose_name='ПИН')
    passport_serial = models.CharField(max_length=2, verbose_name='Серия паспорта',  null=True, blank=True)
    passport_number = models.CharField(max_length=7, verbose_name='Номер паспорта',  null=True, blank=True)
    issue_organ = models.CharField(max_length=200, verbose_name='Место выдачи',  null=True, blank=True)
    issue_data = models.DateField(verbose_name='Дата выдачи', auto_now_add=False,  null=True, blank=True)
    EDUCATION_CHOICES = (
        ('NS', 'Не указан'),
        ('NOT', 'Нет образование'),
        ('PGE', 'Начальное общее образование'),
        ('BGE', 'Основное общее образование'),
        ('SGE', 'Среднее общее образование'),
        ('SVE', 'Среднее профессиональное образование'),
        ('HEB', 'Высшее образование - бакалавриат'),
        ('HES', 'Высшее образование - специалитет, магистратура'),
        ('HET', 'Высшее образование - подготовка кадров высшей квалификации')
    )
    education = models.CharField(max_length=3, choices=EDUCATION_CHOICES, default='NS', verbose_name='Образование')
    education_place = models.CharField(max_length=200, verbose_name="Место образование",  null=True, blank=True)
    profession = models.CharField(max_length=200, default='Нет профессии', verbose_name='Профессия', null=True)
    job = models.CharField(max_length=200, verbose_name='Работа', default='Не указан',  null=True, blank=True)
    workplace = models.CharField(max_length=200, default='Не указан', verbose_name='Место работы', null=True)
    MARITAL_CHOICES = (
        ('N', 'Не указан'),
        ('SB', 'Холост'),
        ('SG', 'Незамужем'),
        ('MB', 'Женат'),
        ('MG', 'Замужен'),
        ('D', 'Разведен(а)')
    )
    marital_status = models.CharField(max_length=2, choices=MARITAL_CHOICES, default='N', verbose_name='Семейное '
                                                                                                       'положение')
    phone = models.CharField(max_length=40, verbose_name='Номер телефона', blank=True, null=True)
    email = models.CharField(max_length=200, verbose_name='Электронная почта', blank=True, null=True)
    STATUS_CHOICES = (
        ('N', 'Неизвестно'),
        ('D', 'Мертв'),
        ('L', 'Жив')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="N", verbose_name='Статус')
    image = models.ImageField(null=True, blank=True, upload_to="images/persons/",
                              verbose_name='Фото')
    user = models.ForeignKey(Profile, max_length=200, verbose_name='Создал', on_delete=models.PROTECT)
    created = models.DateField(auto_now_add=True, verbose_name='Дата создание')
    remarks = models.TextField(verbose_name='Примечание', null=True, blank=True)

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Люди'
        ordering = ["last_name", "first_name", "patronymic"]

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic


class ContactType(models.Model):
    type_contact = models.CharField(max_length=200, verbose_name='Тип контакта')
    remarks = models.TextField(null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Тип контакт'
        verbose_name_plural = 'Виды контакта'
        ordering = ["type_contact"]

    def __str__(self):
        return self.type_contact


class Contacts(models.Model):
    criminal_id = models.ForeignKey(Criminals, verbose_name='ФИО', on_delete=models.CASCADE)
    type_contact = models.ForeignKey(ContactType, verbose_name='Тип контакта', on_delete=models.PROTECT)
    contact = models.CharField(max_length=200, verbose_name='Контакт')
    remarks = models.TextField(null=True, blank=True, verbose_name='Примечание')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ["criminal_id"]

    def __str__(self):
        return str(self.criminal_id) + '--' + str(self.type_contact) + ':' + self.contact


class CriminalAddresses(models.Model):
    criminal_id = models.ForeignKey(Criminals, verbose_name='ФИО', on_delete=models.CASCADE)
    KIND_CHOICES = (
        ('residence', 'Место проживание'),
        ('registration', 'Место прориски')
    )
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default='registration', verbose_name='Тип адреса')
    region = models.CharField(max_length=20, verbose_name='Регион', null=True, blank=True)
    district = models.CharField(max_length=20, verbose_name='Район', null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True, verbose_name='Город')
    village = models.CharField(max_length=20, null=True, blank=True, verbose_name='Село')
    micro_district = models.CharField(max_length=200, null=True, blank=True, verbose_name='Микрорайон/Жил.массив')
    street = models.CharField(max_length=200, null=True, blank=True, verbose_name='Улица')
    home = models.CharField(max_length=200, null=True, blank=True, verbose_name='Дом')
    date_entry = models.DateField(blank=True, null=True, verbose_name='Дата входа')
    date_release = models.DateField(blank=True, null=True, verbose_name='Дата выхода')
    remarks = models.TextField(null=True, blank=True, verbose_name='Примечание')

    class Meta:
        verbose_name = 'Адресс террориста и экстремиста'
        verbose_name_plural = 'Адреса террористов и экстремистов'
        ordering = ["criminal_id"]

    def __str__(self):
        return str(self.criminal_id) + ' - ' + self.street + ', ' + self.home


class PersonAddresses(models.Model):
    person_id = models.ForeignKey(Persons, verbose_name='ФИО', on_delete=models.CASCADE)
    KIND_CHOICES = (
        ('residence', 'Место проживание'),
        ('registration', 'Место прориски')
    )
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default='registration', verbose_name='Тип адреса')
    region = models.CharField(max_length=20, verbose_name='Регион', null=True, blank=True)
    district = models.CharField(max_length=20, verbose_name='Район', null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True, verbose_name='Город')
    village = models.CharField(max_length=20, null=True, blank=True, verbose_name='Село')
    micro_district = models.CharField(max_length=200, null=True, blank=True, verbose_name='Микрорайон/Жил.массив')
    street = models.CharField(max_length=200, null=True, blank=True, verbose_name='Улица')
    home = models.CharField(max_length=200, null=True, blank=True, verbose_name='Дом')
    date_entry = models.DateField(null=True, verbose_name='Дата входа')
    date_release = models.DateField(null=True, verbose_name='Дата выхода')
    remarks = models.TextField(blank=True, verbose_name='Примечание')

    class Meta:
        verbose_name = 'Адресс Родственника и контактируемого лица'
        verbose_name_plural = 'Адреса Родственников и контактируемых лиц'
        ordering = ["person_id"]

    def __int__(self):
        return self.person_id + ' - ' + self.street + ', ' + self.home


class CriminalsRelatives(models.Model):
    criminal_id = models.ForeignKey(Criminals, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Persons, on_delete=models.CASCADE)
    relation = models.ForeignKey(RelativeRelation, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Родственники'
        verbose_name_plural = 'Родственники'

    def __str__(self):
        return str(self.criminal_id) + '--' + str(self.person_id)


class CriminalsContactPersons(models.Model):
    criminal_id = models.ForeignKey(Criminals, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Persons, on_delete=models.CASCADE)
    relation = models.ForeignKey(ContactRelation, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Контактируемое лицо'
        verbose_name_plural = 'Контактируемые лица'

    def __str__(self):
        return str(self.criminal_id) + '--' + str(self.person_id)
