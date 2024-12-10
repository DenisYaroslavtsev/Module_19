from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from task1.forms import UserRegister
from task1.models import Buyer, Game, News


def func(request):
    return render(request, 'first_page.html')


def shop(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }

    return render(request, 'shop.html', context)


def basket(request):
    return render(request, 'basket.html')


def sign_up_by_django(request):
    Buyers = Buyer.objects.all()
    info = {}
    context = {
        'info': info,
    }

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                user_exists = False
                for buyer in Buyers:
                    if buyer.name == username:
                        user_exists = True
                        break

                if user_exists:
                    info['error'] = 'Пользователь уже существует'
                else:
                    Buyer.objects.create(name=username, balance=0, age=age)
                    return HttpResponse(f'Приветствуем, {username}!')

    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form, 'info': info})


def sign_up_by_html(request):
    users = ['Ivan', 'Polina', 'Alex', 'Balthazar', 'Vladimir']
    info = {}
    context = {
        'info': info,
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users and password == repeat_password and int(age) >= 18:
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

    return render(request, 'registration_page.html', context)


def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': page_obj})
