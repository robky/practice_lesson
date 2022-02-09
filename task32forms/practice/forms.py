from django import forms
from .validators import validate_not_empty
from .models import CD

GENRE_CHOICES = (
    ("R", "Рок"),
    ("E", "Электроника"),
    ("P", "Поп"),
    ("C", "Классика"),
    ("O", "Саундтреки"),
)


class ExchangeForm(forms.Form):
    # name = текстовая строка, не более 100 символов.
    # email = ...
    # title = текстовая строка, не более 100 символов.
    # artist = текстовая строка, не более 40 символов.
    # genre = поле выбора из предустановленных значений.
    # price = числовое поле, десятичные числа; необязательное.
    # comment = многострочное текстовое поле; необязательное.
    name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[validate_not_empty])
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=40)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    price = forms.DecimalField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)
    fields = ('name', 'email', 'title', 'artist', 'genre', 'price', 'comment')

    # Метод-валидатор для поля artist
    def clean_artist(self):
        data = self.cleaned_data['artist']
        if not CD.objects.filter(artist=data).count():
            raise forms.ValidationError(
                'Для обмена может быть допущен только диск, исполнитель'
                'которого уже есть в коллекции владельца сайта!')

        # Метод-валидатор обязательно должен вернуть очищенные данные,
        # даже если не изменил их
        return data
