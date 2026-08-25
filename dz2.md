## Подготовка к работе

* Создать аккаунт на GitHub=
* Установить Git на локальную машину
* Настроить глобальные параметры Git:
```bash
git config --global user.name "Ваше Имя"
git config --global user.email "ваш@email.com"
```
## Часть 1. Создание удаленного репозитория

### Шаг 1. Создание репозитория на GitHub

Зайдите на GitHub и создайте новый репозиторий с названием library-management-system 

Создайте репозиторий без README и .gitignore (пустой)
### Шаг 2. Клонирование репозитория

```bash
# Клонируем созданный репозиторий
git clone https://github.com/ВАШ-ЛОГИН/library-management-system.git
cd library-management-system
```
## Часть 2. Разработка проекта

### Шаг 3. Создание базового кода (main branch)

`Файл: book.py`

```python
from typing import List, Dict, Optional
from datetime import datetime
import json

class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int, isbn: str):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = True
        self.rating: List[int] = []
        self.__created_at = datetime.now()
    
    def get_info(self) -> Dict[str, any]:
        """Возвращает информацию о книге в виде словаря"""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'isbn': self.isbn,
            'available': self.is_available,
            'rating': self.get_average_rating(),
            'created': self.__created_at.strftime("%Y-%m-%d")
        }
    
    def get_average_rating(self) -> float:
        """Возвращает среднюю оценку книги"""
        if not self.rating:
            return 0.0
        return round(sum(self.rating) / len(self.rating), 1)
    
    def add_rating(self, score: int) -> None:
        """Добавляет оценку книге (от 1 до 5)"""
        if 1 <= score <= 5:
            self.rating.append(score)
        else:
            raise ValueError("Рейтинг должен быть от 1 до 5")
    
    def __str__(self) -> str:
        status = "Доступна" if self.is_available else "Занята"
        return f"'{self.title}' by {self.author} ({self.year}) - {status}"
```
```bash
# Добавляем файл в Git
git add book.py
git commit -m "feat: добавить базовый класс Book"
git push origin main
```

### Шаг 4. Создание библиотеки (feature branch: feature/library)

```bash
# Создаем и переключаемся на новую ветку
git checkout -b feature/library
```
`Файл: library.py`

```python
from book import Book
from typing import List, Optional, Dict
from datetime import datetime
import json

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []
        self.borrowed_books: Dict[int, str] = {}  # book_id -> user_name
        self.__opened_at = datetime.now()
    
    def add_book(self, book: Book) -> bool:
        """Добавляет книгу в библиотеку"""
        if any(b.id == book.id for b in self.books):
            return False
        self.books.append(book)
        return True
    
    def remove_book(self, book_id: int) -> bool:
        """Удаляет книгу из библиотеки"""
        for i, book in enumerate(self.books):
            if book.id == book_id:
                if book.is_available:
                    self.books.pop(i)
                    return True
                return False
        return False
    
    def find_book(self, **kwargs) -> List[Book]:
        """Поиск книг по различным критериям"""
        results = []
        for book in self.books:
            match = True
            for key, value in kwargs.items():
                if hasattr(book, key):
                    if getattr(book, key) != value:
                        match = False
                        break
            if match:
                results.append(book)
        return results
    
    def borrow_book(self, book_id: int, user_name: str) -> bool:
        """Выдает книгу пользователю"""
        for book in self.books:
            if book.id == book_id and book.is_available:
                book.is_available = False
                self.borrowed_books[book_id] = user_name
                return True
        return False
    
    def return_book(self, book_id: int) -> bool:
        """Возвращает книгу в библиотеку"""
        for book in self.books:
            if book.id == book_id and not book.is_available:
                book.is_available = True
                self.borrowed_books.pop(book_id, None)
                return True
        return False
    
    def get_statistics(self) -> Dict[str, any]:
        """Получает статистику библиотеки"""
        total = len(self.books)
        available = sum(1 for b in self.books if b.is_available)
        borrowed = total - available
        
        avg_rating = 0.0
        if total > 0:
            total_rating = sum(b.get_average_rating() for b in self.books)
            avg_rating = round(total_rating / total, 1)
        
        return {
            'total_books': total,
            'available': available,
            'borrowed': borrowed,
            'average_rating': avg_rating,
            'opened': self.__opened_at.strftime("%Y-%m-%d %H:%M")
        }
```
```bash
git add library.py
git commit -m "feat: добавить класс Library с основным функционалом"
git push origin feature/library
```
### Шаг 5. Создание менеджера книг (feature branch: feature/book-manager)

```bash
git checkout main
git pull
git checkout -b feature/book-manager
```
`Файл: book_manager.py`

```python
from book import Book
from library import Library
from typing import List, Dict, Optional
import json
import csv
import os

class BookManager:
    def __init__(self, library: Library):
        self.library = library
        self.__operation_log: List[str] = []
    
    def add_book_from_json(self, json_file: str) -> int:
        """Добавляет книги из JSON файла"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            added = 0
            for item in data:
                if 'id' in item and 'title' in item and 'author' in item:
                    book = Book(
                        item['id'],
                        item['title'],
                        item['author'],
                        item.get('year', 0),
                        item.get('isbn', 'N/A')
                    )
                    if self.library.add_book(book):
                        added += 1
                        self.__log_operation(f"Добавлена книга: {book.title}")
            
            return added
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {json_file} не найден")
        except json.JSONDecodeError:
            raise ValueError("Неверный формат JSON")
    
    def export_books_to_csv(self, csv_file: str) -> bool:
        """Экспортирует информацию о книгах в CSV"""
        try:
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['ID', 'Название', 'Автор', 'Год', 'ISBN', 'Доступна', 'Рейтинг'])
                
                for book in self.library.books:
                    writer.writerow([
                        book.id,
                        book.title,
                        book.author,
                        book.year,
                        book.isbn,
                        'Да' if book.is_available else 'Нет',
                        book.get_average_rating()
                    ])
            self.__log_operation(f"Экспорт в CSV: {csv_file}")
            return True
        except Exception as e:
            raise RuntimeError(f"Ошибка при экспорте: {e}")
    
    def search_books(self, query: str) -> List[Dict[str, any]]:
        """Поиск книг по текстовому запросу"""
        results = []
        query_lower = query.lower()
        
        for book in self.library.books:
            if (query_lower in book.title.lower() or 
                query_lower in book.author.lower() or 
                query_lower in str(book.year)):
                results.append(book.get_info())
        
        self.__log_operation(f"Поиск: '{query}' найдено {len(results)} книг")
        return results
    
    def __log_operation(self, message: str) -> None:
        """Логирование операций"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__operation_log.append(f"[{timestamp}] {message}")
    
    def get_logs(self) -> List[str]:
        """Возвращает лог операций"""
        return self.__operation_log.copy()
```
```bash
git add book_manager.py
git commit -m "feat: добавить BookManager для управления книгами"
git push origin feature/book-manager
```
## Часть 3. Создание Pull Requests

### Шаг 6. Создание PR для feature/library

На GitHub создайте Pull Request из ветки feature/library в main

Добавьте описание: "Добавлен класс Library с CRUD операциями"

Выполните merge
### Шаг 7. Создание PR для feature/book-manager

Создайте PR из feature/book-manager в main

Добавьте описание: "Добавлен менеджер книг с импортом/экспортом"

Перед merge обновите ветку (resolve conflicts, если есть):
```bash
git checkout feature/book-manager
git pull origin main
# Если есть конфликты - разрешить
git push origin feature/book-manager
```
### Шаг 8. Создание конфликта (Feature: feature/statistics)

```bash
git checkout -b feature/statistics
```
Обновляем library.py (добавляем метод)

```python
    # Добавляем в конец класса Library
    
    def get_statistics(self) -> Dict[str, any]:
        """Получает статистику библиотеки"""
        total = len(self.books)
        available = sum(1 for b in self.books if b.is_available)
        borrowed = total - available
        
        # Добавляем статистику по жанрам (новое поле)
        genres = {}
        for book in self.books:
            # Используем год как приблизительный жанр
            decade = (book.year // 10) * 10
            genres[f"{decade}s"] = genres.get(f"{decade}s", 0) + 1
        
        avg_rating = 0.0
        if total > 0:
            total_rating = sum(b.get_average_rating() for b in self.books)
            avg_rating = round(total_rating / total, 1)
        
        return {
            'total_books': total,
            'available': available,
            'borrowed': borrowed,
            'average_rating': avg_rating,
            'opened': self.__opened_at.strftime("%Y-%m-%d %H:%M"),
            'genres': genres  # новое поле
        }
```
```bash
git add library.py
git commit -m "feat: добавить статистику по годам"
git push origin feature/statistics
```
### Шаг 9. Создание параллельного изменения в main

```bash
git checkout main
git pull
git checkout -b feature/statistics-v2
```
Обновляем library.py (другое изменение)

```python
    # Добавляем в конец класса Library
    
    def get_statistics(self) -> Dict[str, any]:
        """Получает статистику библиотеки"""
        total = len(self.books)
        available = sum(1 for b in self.books if b.is_available)
        borrowed = total - available
        
        # Добавляем статистику по авторам
        authors = {}
        for book in self.books:
            authors[book.author] = authors.get(book.author, 0) + 1
        most_prolific = max(authors.items(), key=lambda x: x[1])[0] if authors else "N/A"
        
        avg_rating = 0.0
        if total > 0:
            total_rating = sum(b.get_average_rating() for b in self.books)
            avg_rating = round(total_rating / total, 1)
        
        return {
            'total_books': total,
            'available': available,
            'borrowed': borrowed,
            'average_rating': avg_rating,
            'opened': self.__opened_at.strftime("%Y-%m-%d %H:%M"),
            'most_prolific_author': most_prolific  # новое поле
        }
```
```bash
git add library.py
git commit -m "feat: добавить статистику по авторам"
git push origin feature/statistics-v2
```
## Часть 4. Разрешение конфликтов

### Шаг 10. Создание PR и разрешение конфликта

Создайте PR для feature/statistics (добавьте описание)

Создайте PR для feature/statistics-v2

При попытке merge второго PR возникнет конфликт

Разрешаем конфликт локально:

```bash
git checkout main
git pull
git checkout feature/statistics-v2
git pull origin main
# Возникнет конфликт в library.py
```
Разрешаем конфликт вручную (объединяем оба изменения):

```python
    def get_statistics(self) -> Dict[str, any]:
        """Получает статистику библиотеки"""
        total = len(self.books)
        available = sum(1 for b in self.books if b.is_available)
        borrowed = total - available
        
        # Статистика по годам (из первой ветки)
        genres = {}
        for book in self.books:
            decade = (book.year // 10) * 10
            genres[f"{decade}s"] = genres.get(f"{decade}s", 0) + 1
        
        # Статистика по авторам (из второй ветки)
        authors = {}
        for book in self.books:
            authors[book.author] = authors.get(book.author, 0) + 1
        most_prolific = max(authors.items(), key=lambda x: x[1])[0] if authors else "N/A"
        
        avg_rating = 0.0
        if total > 0:
            total_rating = sum(b.get_average_rating() for b in self.books)
            avg_rating = round(total_rating / total, 1)
        
        return {
            'total_books': total,
            'available': available,
            'borrowed': borrowed,
            'average_rating': avg_rating,
            'opened': self.__opened_at.strftime("%Y-%m-%d %H:%M"),
            'genres': genres,              # из первой ветки
            'most_prolific_author': most_prolific  # из второй ветки
        }
```
```bash
git add library.py
git commit -m "merge: объединение статистики по годам и авторам"
git push origin feature/statistics-v2
```
## Часть 5. Тестирование

### Шаг 11. Создание тестов

```bash
git checkout -b feature/tests
```
`Файл: test_library.py`

```python
import unittest
from book import Book
from library import Library
from book_manager import BookManager
import json
import tempfile
import os

class TestLibrarySystem(unittest.TestCase):
    
    def setUp(self):
        """Подготовка к каждому тесту"""
        self.library = Library("Test Library")
        self.book1 = Book(1, "1984", "George Orwell", 1949, "978-0451524935")
        self.book2 = Book(2, "Brave New World", "Aldous Huxley", 1932, "978-0060850524")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.manager = BookManager(self.library)
    
    def test_book_creation(self):
        """Тест создания книги"""
        self.assertEqual(self.book1.title, "1984")
        self.assertEqual(self.book1.author, "George Orwell")
        self.assertTrue(self.book1.is_available)
    
    def test_add_rating(self):
        """Тест добавления оценок"""
        self.book1.add_rating(5)
        self.book1.add_rating(4)
        self.assertEqual(self.book1.get_average_rating(), 4.5)
        
        with self.assertRaises(ValueError):
            self.book1.add_rating(10)
    
    def test_borrow_book(self):
        """Тест выдачи книги"""
        self.assertTrue(self.library.borrow_book(1, "Иван"))
        self.assertFalse(self.book1.is_available)
        self.assertIn(1, self.library.borrowed_books)
        self.assertEqual(self.library.borrowed_books[1], "Иван")
        
        # Нельзя выдать уже занятую книгу
        self.assertFalse(self.library.borrow_book(1, "Петр"))
    
    def test_return_book(self):
        """Тест возврата книги"""
        self.library.borrow_book(1, "Иван")
        self.assertTrue(self.library.return_book(1))
        self.assertTrue(self.book1.is_available)
        self.assertNotIn(1, self.library.borrowed_books)
    
    def test_search_books(self):
        """Тест поиска книг"""
        results = self.manager.search_books("Orwell")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "1984")
    
    def test_statistics(self):
        """Тест статистики"""
        stats = self.library.get_statistics()
        self.assertEqual(stats['total_books'], 2)
        self.assertEqual(stats['available'], 2)
        self.assertEqual(stats['borrowed'], 0)
        
        self.library.borrow_book(1, "Иван")
        stats = self.library.get_statistics()
        self.assertEqual(stats['available'], 1)
        self.assertEqual(stats['borrowed'], 1)
    
    def test_export_import(self):
        """Тест экспорта/импорта"""
        # Экспорт
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            csv_file = f.name
        
        try:
            self.manager.export_books_to_csv(csv_file)
            self.assertTrue(os.path.exists(csv_file))
            
            # Проверяем, что файл не пустой
            with open(csv_file, 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertTrue(len(content) > 0)
        finally:
            os.unlink(csv_file)

if __name__ == '__main__':
    unittest.main()
```
```bash
git add test_library.py
git commit -m "test: добавить юнит-тесты для библиотеки"
git push origin feature/tests
```
## Часть 6. Заключительные шаги

### Шаг 12. Финальный merge

Создайте PR для feature/tests

После проверки объедините с main

### Шаг 13. Обновление локального репозитория

```bash
git checkout main
git pull origin main
```

## Полезные команды для справки:

```bash
# Просмотр статуса
git status

# Просмотр истории
git log --oneline --graph --all

# Просмотр изменений
git diff

# Переключение между ветками
git checkout <branch-name>

# Создание и переключение на ветку
git checkout -b <new-branch>

# Получение изменений с удаленного репозитория
git fetch

# Слияние веток
git merge <branch-name>

# Отмена изменений (быть осторожным!)
git reset --hard HEAD~1. 
```