from django.contrib import admin
from .models import *
# Register your models here.

# класс для транслита ссылок
class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}  # для транслита: прописываем словарь, имя обязательное, slag наследуется от....
# класс преобразования модели Gallery в панели
class PortfolioAdmin(admin.ModelAdmin):   # имена у переменных приведенных в этом классе обязательны
    list_display = ('title', 'cat')     # кортеж с именами полей для названия записей в списке
    search_fields = ('title', )  # поля для поиска, в данном случае по названию (см. models.py), кортеж с одним значением, поэтому зпт и пробел
    # list_display_links = () поля в виде ссылок по которым можно переходить в БД

# регистрация моделей
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Portfolio, PortfolioAdmin)