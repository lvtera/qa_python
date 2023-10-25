from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_when_already_in_collection(self):
        collector = BooksCollector()

        collector.add_new_book('Бесконечная шутка')
        collector.add_new_book('Бесконечная шутка')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_no_genre_by_default(self):
        collector = BooksCollector()

        collector.add_new_book('Улисс')

        assert collector.get_book_genre('Улисс') == ''

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Незнайка на луне', 'Мультфильмы'],
            ['Пикник на обочине', 'Фантастика'],
            ['Ревизор', 'Комедии'],
            ['Зов Ктулху', 'Ужасы'],
            ['Десять негритят', 'Детективы']
        ]
    )
    def test_set_book_genre_all_genres(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Золушка', 'Мультфильмы'],
            ['Солярис', 'Фантастика'],
            ['Двенадцать стульев', 'Комедии'],
            ['Оно', 'Ужасы'],
            ['Собака Баскервилей', 'Детективы']
        ]
    )
    def test_get_book_genre_all_genres(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Незнайка на луне', 'Мультфильмы'],
            ['Пикник на обочине', 'Фантастика'],
            ['Ревизор', 'Комедии'],
            ['Зов Ктулху', 'Ужасы'],
            ['Десять негритят', 'Детективы']
        ]
    )
    def test_get_books_with_specific_genre_all_genres(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_for_children_from_all_genres(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
        collector.add_new_book('Имя розы')
        collector.set_book_genre('Имя розы', 'Детектив')
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')


        assert collector.get_books_for_children() == ['Дюна', 'Незнайка на луне', 'Ревизор']

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Шатуны')
        collector.add_book_in_favorites('Шатуны')

        assert collector.get_list_of_favorites_books() == ['Шатуны']

    def test_add_book_in_favorites_same_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гроза')
        collector.add_book_in_favorites('Гроза')
        collector.add_book_in_favorites('Гроза')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Пчела-попаданец')
        collector.add_book_in_favorites('Пчела-попаданец')
        collector.delete_book_from_favorites('Пчела-попаданец')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')

        assert collector.get_list_of_favorites_books() == ['Война и мир']
