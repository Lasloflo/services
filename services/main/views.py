from django.shortcuts import render, redirect
from message.models import Message
from message.forms import MessageForm
from portfolio.models import Categorie, Portfolio
from team.models import Team
from interaction.models import Interaction, Object

# Create your views here.
def index(request):
    portfolio_cat = Categorie.objects.all()
    portfolio = Portfolio.objects.all()
    interaction_con = Interaction.objects.all()
    object_int = Object.objects.all()
    data = {
        'portfolio_cat': portfolio_cat,
        'portfolio': portfolio,
        'counter1': 67,
        'counter2': 130,
        'counter3': 27159,
        'interaction_con': interaction_con,
        'object_int': object_int,
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
    team = Team.objects.all()
    interaction_con = Interaction.objects.all()
    object_int = Object.objects.all()
    data = {'team': team,
            'interaction_con': interaction_con,
            'object_int': object_int,
            }
    return render(request, 'main/about.html', data)

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
            error_form = 'Некорректные данные! Неверно указан адрес электроннной почты или номер телефона.'  # передаем в словарь data для возможности вывода на сайт

    message_form = MessageForm()
    data = {
        # 'gallery_cat': gallery_cat,
        # 'gallery': gallery,
        # 'title': 'ЕДА',  # передаем название страницы
        # 'favicon': 'static/img/favicon.ico',  # передаём путь к фавикону
        # 'menu': menu,  # ссылка на словарь menu, описанный выше
        # 'phone': '+375-29-9145208',  # номер телефона в Контактах, написанных на странице
        'email': 'beltiar_t@tut.by l.plotnikova.v@gmail.com',  # электронка в Контактах, написанных на странице
        'address': 'Минская область, г.Дзержинск, ул.Советская, д.5, п.14',
        'day_working': 'Работаем пн-пт',
        'working_time1': '08.00 - 13.00',
        'working_time2': '14.00 - 17.00',
        'phone': '+375-33-300-00-20 +375-29-627-26-83',
        'phone2': '8-01718-ХХ-Х-ХХ',
        # 'menu_cat': menu_cat,
        # 'dishes': dishes,
        # 'about': about,
        # 'about_image': 'static/img/about.jpg',
        # 'our_restaurant': '',  # но, наверно, я ввод текста на сайте из словаря не делала...
        # 'feedbacks': feedback,
        'message_form': message_form,
        'error_form': error_form}
    return render(request, 'main/contact.html', data)

def branch(request):
    error_form = ''  # изначально текст ошибки пустой
    # обработка post-запроса; # request.POST формируется как словарь
    if request.method == 'POST':  # если пост запрос был
        message_form = MessageForm(request.POST)  # создается экземпляр класса с данными, переданными пользователем
        if message_form.is_valid():  # если форма заполнена правильно
            message_form.save()  # сохраняем
            return redirect('branch.html')
        else:
            error_form = 'Некорректные данные! Неверно указан адрес электроннной почты или номер телефона.'

    message_form = MessageForm()
    data = {
        'email': 'stolbcy_mail@tut.by l.plotnikova.v@gmail.com',
        'address': 'Минская область, г.Столбцы, ул.Социалистическая, д.28',
        'day_working': 'Работаем пн-пт',
        'working_time1': '08.00 - 13.00',
        'working_time2': '14.00 - 17.00',
        'phone': '+375-29-769-45-96',
        'phone2': '8-01717-70-9-26',
        'message_form': message_form,
        'error_form': error_form}
    return render(request, 'main/branch.html', data)

