from django.shortcuts import render, redirect
from message.models import Message
from message.forms import MessageForm
from portfolio.models import *

# Create your views here.
def index(request):
    portfolio_cat = Categorie.objects.all()
    portfolio = Portfolio.objects.all()
    data = {
        'portfolio_cat': portfolio_cat,  # галерея блюд
        'portfolio': portfolio,
        # 'title': 'ЕДА',  # передаем название страницы
        # 'favicon': 'static/img/favicon.ico',  # передаём путь к фавикону
        # 'menu': menu,  # ссылка на словарь menu, описанный выше
        # 'phone': '+375-29-9145208',  # номер телефона в Контактах, написанных на странице
        # 'menu_cat': menu_cat,
        # 'dishes': dishes,
        # 'about': about,
        # 'about_image': 'static/img/about.jpg',
        # 'our_restaurant': '',  # но, наверно, я ввод текста на сайте из словаря не делала...
        # 'feedbacks': feedback,
        }
    return render(request, 'main/index.html', data)

def work(request):
    portfolio_cat = Categorie.objects.all()
    portfolio = Portfolio.objects.all()
    data = {
        'portfolio_cat': portfolio_cat,  # галерея блюд
        'portfolio': portfolio,
        }
    return render(request, 'main/work.html', data)

def order(request):
    return render(request, 'main/order.html')
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    # вывод ошибки, если поле заполненно некорректно
    error_form = ''  # изначально текст ошибки пустой
    # обработка post-запроса; # request.POST формируется как словарь
    if request.method == 'POST':  # если пост запрос был
        message_form = MessageForm(request.POST)  # создается экземпляр класса с данными, переданными пользователем
        if message_form.is_valid():  # если форма заполнена правильно
            message_form.save()  # сохраняем
            return redirect('contact.html')
        else:
            error_form = 'Неверные данные в форме отправки сообщения!'  # передаем в словарь data для возможности вывода на сайт
            # error_dict = {'error_form': error_form}
            # return redirect('contact.html', error_dict)
    message_form = MessageForm()
    data = {
        # 'gallery_cat': gallery_cat,  # галерея блюд
        # 'gallery': gallery,
        # 'title': 'ЕДА',  # передаем название страницы
        # 'favicon': 'static/img/favicon.ico',  # передаём путь к фавикону
        # 'menu': menu,  # ссылка на словарь menu, описанный выше
        # 'phone': '+375-29-9145208',  # номер телефона в Контактах, написанных на странице
        'email': 'beltiar_t@tut.by beltiar_t@tut.by beltiar_t@tut.by beltiar_t@tut.by beltiar_t@tut.by beltiar_t@tut.by',  # электронка в Контактах, написанных на странице
        'address': 'Минская область, г.Дзержинск, ул.Советская, д.5.',
        'phone': '+375-33-300-00-20 +375-29-627-26-83 +375-33-300-00-20 +375-29-627-26-83',
        'phone2': '+375-29-2568011 +375-29-2568011',
        # 'menu_cat': menu_cat,
        # 'dishes': dishes,
        # 'about': about,
        # 'about_image': 'static/img/about.jpg',
        # 'our_restaurant': '',  # но, наверно, я ввод текста на сайте из словаря не делала...
        # 'feedbacks': feedback,
        'message_form': message_form,
        'error_form': error_form}

    return render(request, 'main/contact.html', data)

