from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ExchangeForm


def send_msg(email, name, title, artist, genre, price, comment):
    subject = f"Обмен {artist}-{title}"
    body = f"""Предложение на обмен диска от {name} ({email})

    Название: {title}
    Исполнитель: {artist}
    Жанр: {genre}
    Стоимость: {price}
    Комментарий: {comment}

    """
    send_mail(
        subject, body, email, ["admin@rockenrolla.net", ],
    )


def index(request):
    # После заполнения формы показывайте шаблон "thankyou.html"
    # Проверяем, получен POST-запрос или какой-то другой:
    if request.method == 'POST':
        # Создаём объект формы класса ContactForm
        # и передаём в него полученные данные
        form = ExchangeForm(request.POST)

        # Если все данные формы валидны - работаем с "очищенными данными" формы
        if form.is_valid():
            # Берём валидированные данные формы из словаря form.cleaned_data
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            artist = form.cleaned_data['artist']
            genre = form.cleaned_data['genre']
            price = form.cleaned_data['price']
            comment = form.cleaned_data['comment']

            # При необходимости обрабатываем данные
            send_msg(email, name, title, artist, genre, price, comment)

            # Функция redirect перенаправляет пользователя
            return redirect('/thank-you/')

        # Если условие if form.is_valid() ложно и данные не прошли валидацию -
        # передадим полученный объект в шаблон,
        # чтобы показать пользователю информацию об ошибке

        # Заодно заполним все поля формы данными, прошедшими валидацию,
        # чтобы не заставлять пользователя вносить их повторно
        return render(request, 'index.html', {'form': form})

    # Если пришёл не POST-запрос - создаём и передаём в шаблон пустую форму
    # пусть пользователь напишет что-нибудь
    form = ExchangeForm()
    return render(request, 'index.html', {'form': form})


def thank_you(request):
    template = 'thankyou.html'
    return render(request, template)
