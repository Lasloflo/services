from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Message(models.Model):
    THEME_CHOICES = (('Заключение договора','Заключение договора'), ('Отзыв','Отзыв'), ('Иное...','Иное...'))
    theme = models.CharField('тема сообщения', max_length=20, choices=THEME_CHOICES)
    name = models.CharField('имя', max_length=35)
    email = models.EmailField('e-mail')
    phone = PhoneNumberField('телефон')
    message = models.TextField('сообщение')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.name