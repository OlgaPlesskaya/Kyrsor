from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
# Create your models here.

class Vuz_1(models.Model):
    id = models.CharField("ID", max_length=255, primary_key=True)
    name = models.CharField("Название ВУЗа", max_length=255)
    short_name = models.CharField("Короткое название ВУЗа",max_length=255)
    url = models.CharField("Сайт ВУЗа", max_length=255)
    logo = models.ImageField("Логотип", upload_to='вузы/')
    obr_pr = models.IntegerField("Образовательных программ")
    pr_b = models.IntegerField("Минимальный проходной балл")
    bm = models.IntegerField("Бюджетных мест")
    adress = models.CharField("Адрес", max_length=255, default='')
    coordinates = models.CharField("Координаты", max_length=255, default='')
    latitude= models.CharField("Широта", max_length=255, default='')
    longitude = models.CharField("Долгота", max_length=255, default='')
    metro_name = models.CharField("Название станции метро", max_length=255, default='')
    metro_latitude = models.CharField("Широта метро", max_length=255, default='')
    metro_longitude = models.CharField("Долгота метро", max_length=255, default='')
    name_metro = models.CharField("Название станции метро", max_length=255, default='')
    distance_to_metro = models.FloatField("Расстояние от главного корпуса до метро", default='')
    # distance_from_metro = models.FloatField("Расстояние до метро")
    # distance_from_dormitory = models.FloatField("Расстояние до общежития")
    distance_between_buildings = models.FloatField(null=True, blank=True)
    distance_from_dormitory = models.FloatField("Расстояние до общежития от гл корп",null=True, blank=True)

    # url = models.SlugField(max_length=160)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vuz_detail",kwargs={"pk": self.id})

    class Meta:
        verbose_name_plural = "Вузы"

class Comments(models.Model):
    """Отзывы"""
    comment_id = models.AutoField(primary_key=True)
    name = models.ForeignKey(Vuz_1,verbose_name="Название ВУЗа", on_delete=models.CASCADE)
    text = models.TextField("Текст отзыва",max_length=5000)
    rait = models.FloatField("Оценка", default='' )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Comments_1(models.Model):
    """Отзывы"""
    id = models.CharField("ID", max_length=255, primary_key=True)
    name = models.ForeignKey(Vuz_1, verbose_name="Название ВУЗа", on_delete=models.CASCADE)
    text = models.TextField("Текст отзыва", max_length=5000)
    rait = models.FloatField("Оценка")
    date = models.DateTimeField("Дата оставления", auto_now_add=True)


class Comments_2(models.Model):
    """Отзывы"""
    id = models.AutoField("ID", primary_key=True)
    name = models.ForeignKey(Vuz_1, verbose_name="Название ВУЗа", on_delete=models.CASCADE)
    text_1 = models.TextField("Учеба", max_length=5000, blank=True, default='')
    rait_1 = models.IntegerField("Оценка_учеба")
    text_2 = models.TextField("Преподаватели", max_length=5000, blank=True, default='')
    rait_2 = models.IntegerField("Оценка_преподаватели")
    text_3 = models.TextField("Студенческая жизнь", max_length=5000, blank=True, default='')
    rait_3 = models.IntegerField("Оценка_студенческая жизнь")
    text_4 = models.TextField("Расположение", max_length=5000, blank=True, default='')
    rait_4 = models.IntegerField("Оценка_расположение")
    text_5 = models.TextField("Общежитие", max_length=5000, blank=True, default='')
    rait_6 = models.IntegerField("Оценка_общежитие")
    rait = models.IntegerField("Оценка_общая")
    date = models.DateTimeField("Дата оставления", auto_now_add=True)

class Department(models.Model):
    """Факультеты"""
    id = models.AutoField("ID", primary_key=True)
    name = models.ForeignKey(Vuz_1, verbose_name="Название ВУЗа", on_delete=models.CASCADE)
    department = models.TextField("Факультет", max_length=250)

class Programms(models.Model):
    """Факультеты"""
    id = models.AutoField("ID", primary_key=True)
    name = models.ForeignKey(Vuz_1, verbose_name="Название ВУЗа", on_delete=models.CASCADE)
    programm = models.TextField("Направление подготовки программы", max_length=250)
    passing_score = models.IntegerField("Проходной балл на очное в 2023 году",null=True, blank=True)
    budget_places = models.IntegerField("Бюджетных мест на очное в 2024 году",null=True, blank=True)
    cost_of_education = models.IntegerField("Стоимость обучения очное",null=True, blank=True)
    сod_programm = models.TextField("Код программы", max_length=250)

class Dormitory(models.Model):
    """Общежития"""
    id = models.AutoField("ID", primary_key=True)
    name = models.ForeignKey(Vuz_1, verbose_name="Название ВУЗа", on_delete=models.CASCADE)
    latitude = models.CharField("Широта", max_length=255, default='')
    longitude = models.CharField("Долгота", max_length=255, default='')

class University_buildings(models.Model):
    """Корпуса ВУЗов"""
    id = models.AutoField("ID", primary_key=True)
    name = models.ForeignKey(Vuz_1, verbose_name="Название ВУЗа", on_delete=models.CASCADE)
    latitude = models.CharField("Широта", max_length=255, default='')
    longitude = models.CharField("Долгота", max_length=255, default='')