# simple-shop
Вопросы преподавателю:
1. Каким образом маркировать товары типа "Фуфайка"?
    1. М.б. завести категорию с признаком "непрофильные товары"?
    1. Возможно ли отнаследоваться от класса Product в класс Одежда?

План работ по дипломному проекту
1. Реализовать метод для отображения цены в формате # ##0.00
1. Отмаркировать товары типа "Фуфайка", сделать отображение на главной странице
1. Уточнить требуемый функционал к админской части
    * Отображать в админке в форме product m2m-связь с пользователями через корзину
1. Сделать в хедере стилистическое отображение `username`
1. Переделать пагинацию на `form` и `ListView`
    * Решить вопрос по стилистическомиу отображению стрелок в пагинации
1. Переделать меню на `form`
1. Обновить загрузку фикстур в обе стороны
1. Протестировать корзину на нескольких пользователях
* Реализовать механизм анонимных отзывов как показано на макете [Страница товара](resources/product.html).
* Реализовать возможность регистрации по почте (без подтверждения почты).

Улучшить:
1. В шаблоне реализовано только двухуровневное меню
1. Нет проверки на то, что товары д.б. только в "конечных" категориях
1. При параметриазации url'ов не добавлена проверка на правильность типа данных

Сделано:
1. аутентификация пользователей
1. общий код всех шаблонов выведен в *base.html*
1. пагинация на странице category.html
1. Реализована древовидная структура категорий товаров
1. Для отображения товаров на главной странице сделан признак for_main
1. Создан параметризованный url отображения на странице category.html требуемой категории товаров
1. Реализован функционал корзины
1. Если пользователь не атворизован, по кнопкам "Корзина" и "Добавить в корзину" переадресовывать на страницу авторизации
1. Решена проблема с хранением изображений
1. Реализована страница детальной информации о товаре
1. Перенести функционал корзины в отдельное приложение
