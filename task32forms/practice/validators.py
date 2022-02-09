# Функция-валидатор:
def validate_not_empty(value):
    # Проверка "а заполнено ли поле?"
    if value == '':
        raise forms.ValidationError(
            'А кто поле будет заполнять, Пушкин?',
            params={'value': value},
        )
