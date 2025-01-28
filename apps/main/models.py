from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип"
    )
    
    def str(self):
        return self.title   
    
    class Meta:
        verbose_name= "Настройка"
        verbose_name_plural= "Настройки"

class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Главное"
        verbose_name_plural = "Главное"

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    video = models.FileField(
        upload_to="video/",
        verbose_name='Видео'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Contact(models.Model):
     title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
     description = models.TextField(
        verbose_name="Описание"
    )
     email = models.EmailField(
        verbose_name="EMail"
    )
     adress = models.CharField(
        max_length=255,
        verbose_name="Адрес"
     )
     phone = models.BigIntegerField(
        verbose_name="Номер телефона"
     )
     def __str__(self):
        return self.title
    
     class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

class Form(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя отправителя"
    )
    email = models.EmailField(
        verbose_name="Email отправителя"
    )
    message = models.TextField(
        verbose_name="Сообщение"
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Оставленный отзыв"
        verbose_name_plural = "Оставленный отзыв"